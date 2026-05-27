# 龚亚夫智能体 - 部署与使用指南

## 项目简介

龚亚夫智能体是一个面向学校英语教师的AI对话助手，基于龚亚夫老师全部教学理念构建。教师通过苏格拉底式对话，深入理解任务型语言教学、多元目标英语课程、英语课程标准等核心知识。

### 核心特征

- **知识边界严格**：仅依据龚亚夫老师三本著作及教学理念回答，不搜罗网络信息
- **苏格拉底式对话**：不直接给答案，通过追问引导教师自己发现和建构理解
- **话题边界守卫**：拒绝回答与英语教学无关的问题
- **三层九维诊断**：基于龚亚夫多元目标框架进行教学分析

## 技术架构

```
gongyafu-agent/
├── main.py                  # FastAPI 入口
├── config.yaml              # 配置文件（API密钥、模型等）
├── requirements.txt         # Python依赖
├── agent/
│   ├── __init__.py
│   ├── system_prompt.py     # 核心系统提示词（龚亚夫人格+知识+约束）
│   ├── knowledge_base.py    # 三书知识库（结构化）
│   ├── dialogue_engine.py   # 苏格拉底对话引擎
│   ├── boundary_guard.py    # 话题边界守卫
│   └── response_formatter.py # 响应格式化
├── data/
│   └── knowledge.json       # 结构化知识数据
└── static/
    └── index.html           # 聊天界面
```

## 快速部署

### 1. 安装依赖

```bash
cd gongyafu-agent
pip install -r requirements.txt
```

### 2. 配置API

编辑 `config.yaml`，填入你的LLM API信息：

```yaml
llm:
  api_key: "your-api-key-here"
  base_url: "https://api.openai.com/v1"   # 或其他兼容接口
  model: "gpt-4o"                          # 或其他模型
```

### 3. 启动服务

```bash
python main.py
```

服务默认运行在 `http://localhost:8900`

### 4. 访问界面

浏览器打开 `http://localhost:8900` 即可使用。

## API接口

### 对话接口

```
POST /api/chat
Content-Type: application/json

{
  "message": "任务型语言教学和传统教学有什么区别？",
  "session_id": "optional-session-id"
}
```

响应：

```json
{
  "reply": "你提到了'区别'，这是个很好的出发点。在你看来，传统英语教学最典型的做法是什么？",
  "session_id": "abc123",
  "is_on_topic": true,
  "dialogue_stage": "probing"
}
```

### 健康检查

```
GET /api/health
```

## 约束条件说明

| 约束类型 | 规则 | 处理方式 |
|---------|------|---------|
| 知识边界 | 仅使用龚亚夫老师三本书内容 | 不引用外部来源 |
| 话题边界 | 只回答英语教学相关问题 | 对无关话题温和拒绝并引导回教学 |
| 对话方式 | 苏格拉底式追问 | 不直接给出结论 |
| 理论深度 | 基于三层九维框架分析 | 每次追问指向具体维度 |
| 身份边界 | 以龚亚夫教学思想为基底 | 不替代真实龚亚夫老师 |

## 知识来源

1. **《英语教育新论：多元目标英语课程》**（高等教育出版社，2015）
2. **《任务型语言教学》修订版**（人民教育出版社，2006）
3. **《义务教育英语课程标准（2022年版）案例式解读》**（华东师大出版社，2023）
