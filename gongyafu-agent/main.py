"""
龚亚夫教学智能体 - FastAPI 主程序
可部署到本地服务器的AI对话服务
"""

import os
import json
import uuid
import yaml
import httpx
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel
from typing import Optional, Dict, Any, List

from agent import (
    SYSTEM_PROMPT, KNOWLEDGE_BASE,
    is_teaching_related, get_redirection_message,
    DialogueEngine, DialogueStage, format_response,
)

# ─── 加载配置 ───────────────────────────────────────
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.yaml")
with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    CONFIG = yaml.safe_load(f)

LLM_CONFIG = CONFIG["llm"]
AGENT_CONFIG = CONFIG["agent"]

# ─── 初始化 ─────────────────────────────────────────
app = FastAPI(title="龚亚夫教学智能体", version="1.0.0")
dialogue_engine = DialogueEngine(
    max_probing_rounds=AGENT_CONFIG.get("max_probing_rounds", 3),
    min_probing_rounds=AGENT_CONFIG.get("min_probing_rounds", 1),
)

# 会话存储（生产环境应替换为Redis/数据库）
sessions: Dict[str, Dict[str, Any]] = {}

# 构建知识库摘要（注入系统提示词）
KNOWLEDGE_SUMMARY = _build_knowledge_summary() if False else ""


# ─── 数据模型 ───────────────────────────────────────
class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None


class ChatResponse(BaseModel):
    reply: str
    session_id: str
    is_on_topic: bool
    dialogue_stage: str
    probing_count: int
    goal_dimension: Optional[str] = None


# ─── 核心逻辑 ───────────────────────────────────────
def get_or_create_session(session_id: Optional[str]) -> Dict[str, Any]:
    """获取或创建会话"""
    if session_id and session_id in sessions:
        return sessions[session_id]
    
    new_id = session_id or str(uuid.uuid4())
    sessions[new_id] = {
        "id": new_id,
        "history": [],           # 对话历史 [{"role": "user/assistant", "content": "..."}]
        "probing_count": 0,      # 当前追问轮数
        "stage": "init",         # 对话阶段
        "topics_discussed": [],  # 已讨论的话题维度
    }
    return sessions[new_id]


async def call_llm(messages: List[Dict[str, str]]) -> str:
    """调用LLM API"""
    url = f"{LLM_CONFIG['base_url']}/chat/completions"
    headers = {
        "Authorization": f"Bearer {LLM_CONFIG['api_key']}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": LLM_CONFIG["model"],
        "messages": messages,
        "temperature": LLM_CONFIG.get("temperature", 0.7),
        "max_tokens": LLM_CONFIG.get("max_tokens", 2048),
    }
    
    async with httpx.AsyncClient(timeout=LLM_CONFIG.get("timeout", 60)) as client:
        response = await client.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]


def build_messages(session: Dict[str, Any], user_message: str) -> List[Dict[str, str]]:
    """构建发送给LLM的消息列表"""
    # 获取当前对话阶段指令
    stage = DialogueStage(session["stage"])
    stage_instruction = dialogue_engine.get_stage_instruction(stage)
    
    # 构建系统提示词
    system_content = SYSTEM_PROMPT
    
    # 添加当前阶段指令
    if stage_instruction:
        system_content += f"\n\n---\n\n# 当前对话阶段指令\n\n{stage_instruction}"
    
    # 添加知识约束提醒
    system_content += (
        "\n\n---\n\n# 重要提醒\n\n"
        "- 你只能依据龚亚夫老师三本著作的教学理念回答问题\n"
        "- 不要搜索或引用任何网络来源\n"
        "- 不要使用龚亚夫著作以外的理论框架\n"
        "- 保持苏格拉底式追问风格，不直接给长篇答案\n"
        "- 回答控制在200-400字"
    )
    
    messages = [{"role": "system", "content": system_content}]
    
    # 添加对话历史（最近10轮）
    history = session["history"][-20:]  # 最近20条消息（约10轮）
    messages.extend(history)
    
    # 添加当前用户消息
    messages.append({"role": "user", "content": user_message})
    
    return messages


async def process_chat(message: str, session_id: Optional[str] = None) -> ChatResponse:
    """处理聊天请求"""
    # 1. 获取/创建会话
    session = get_or_create_session(session_id)
    sid = session["id"]
    
    # 2. 边界守卫：检查话题相关性
    if not is_teaching_related(message):
        return ChatResponse(
            reply=get_redirection_message(),
            session_id=sid,
            is_on_topic=False,
            dialogue_stage=session["stage"],
            probing_count=session["probing_count"],
        )
    
    # 3. 记录用户消息到历史
    session["history"].append({"role": "user", "content": message})
    
    # 4. 构建消息并调用LLM
    messages = build_messages(session, message)
    
    try:
        reply = await call_llm(messages)
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=502, detail=f"LLM API调用失败: {e}")
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="LLM API调用超时")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"内部错误: {str(e)}")
    
    # 5. 记录助手回复到历史
    session["history"].append({"role": "assistant", "content": reply})
    
    # 6. 更新对话状态
    current_stage = DialogueStage(session["stage"])
    if current_stage == DialogueStage.INIT:
        session["stage"] = DialogueStage.LISTENING.value
    elif current_stage == DialogueStage.LISTENING:
        session["stage"] = DialogueStage.PROBING_L1.value
        session["probing_count"] = 1
    elif current_stage.value.startswith("probing"):
        session["probing_count"] += 1
        if session["probing_count"] >= AGENT_CONFIG.get("max_probing_rounds", 3):
            session["stage"] = DialogueStage.SCAFFOLDING.value
        else:
            # 升级追问层次
            stage_order = [
                DialogueStage.PROBING_L1,
                DialogueStage.PROBING_L2,
                DialogueStage.PROBING_L3,
            ]
            try:
                idx = [s.value for s in stage_order].index(session["stage"])
                if idx < len(stage_order) - 1:
                    session["stage"] = stage_order[idx + 1].value
            except ValueError:
                pass
    elif current_stage == DialogueStage.SCAFFOLDING:
        session["stage"] = DialogueStage.CONFIRMING.value
    elif current_stage == DialogueStage.CONFIRMING:
        session["stage"] = DialogueStage.COMPLETE.value
    elif current_stage == DialogueStage.COMPLETE:
        # 新话题重置
        session["stage"] = DialogueStage.LISTENING.value
        session["probing_count"] = 0
    
    # 7. 识别涉及的维度（简单关键词匹配）
    goal_dimension = None
    dimension_keywords = {
        "社会文化": ["社会文化", "行为规范", "美德", "多元文化", "国际意识", "学科融合"],
        "思维认知": ["思维认知", "思维能力", "成长型思维", "学习策略", "元认知"],
        "语言交流": ["语言交流", "语言知识", "语言技能", "沟通策略", "交际"],
    }
    for dim, keywords in dimension_keywords.items():
        if any(kw in message for kw in keywords):
            goal_dimension = dim
            break
    
    return ChatResponse(
        reply=reply,
        session_id=sid,
        is_on_topic=True,
        dialogue_stage=session["stage"],
        probing_count=session["probing_count"],
        goal_dimension=goal_dimension,
    )


# ─── API路由 ─────────────────────────────────────────
@app.post("/api/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """对话接口"""
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="消息不能为空")
    return await process_chat(request.message, request.session_id)


@app.get("/api/health")
async def health_check():
    """健康检查"""
    return {
        "status": "ok",
        "agent": AGENT_CONFIG["name"],
        "sessions": len(sessions),
        "llm_model": LLM_CONFIG["model"],
    }


@app.get("/api/sessions/{session_id}")
async def get_session(session_id: str):
    """获取会话信息"""
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="会话不存在")
    s = sessions[session_id]
    return {
        "session_id": s["id"],
        "stage": s["stage"],
        "probing_count": s["probing_count"],
        "message_count": len(s["history"]),
        "topics": s["topics_discussed"],
    }


@app.delete("/api/sessions/{session_id}")
async def delete_session(session_id: str):
    """删除会话"""
    if session_id in sessions:
        del sessions[session_id]
    return {"status": "deleted"}


# ─── 静态文件和页面 ─────────────────────────────────
static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/", response_class=HTMLResponse)
async def index():
    """聊天界面"""
    index_path = os.path.join(static_dir, "index.html")
    return FileResponse(index_path)


# ─── 启动 ───────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    host = CONFIG["server"]["host"]
    port = CONFIG["server"]["port"]
    debug = CONFIG["server"]["debug"]
    print(f"🏛️  龚亚夫教学智能体启动中...")
    print(f"📍 地址: http://localhost:{port}")
    print(f"🤖 模型: {LLM_CONFIG['model']}")
    print(f"📚 知识来源: 龚亚夫三本著作（仅限）")
    print(f"🔒 话题边界: 仅英语教学")
    uvicorn.run("main:app", host=host, port=port, reload=debug)
