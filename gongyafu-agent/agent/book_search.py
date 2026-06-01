"""
龚亚夫智能体 - 本地文本检索模块
基于4本书的OCR提取文本，提供关键词检索功能
当用户提问时，搜索相关段落注入上下文
"""

import os
import re
import json
from typing import List, Dict, Optional, Tuple

# 4本书的原始文本路径（相对于项目根目录）
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_BOOKS_DIR = os.path.join(_PROJECT_ROOT, "data", "raw_books")

BOOK_FILES = {
    "tblt": "任务型语言教学197.md",
    "bfee1": "基础外语教育与研究 第一辑-204.md",
    "bfee2": "基础外语教育与研究 第二辑-204.md",
    "case_primary": "案例式解读小学分册-237.md",
}

BOOK_TITLES = {
    "tblt": "《任务型语言教学》",
    "bfee1": "《基础外语教育与研究 第一辑》",
    "bfee2": "《基础外语教育与研究 第二辑》",
    "case_primary": "《案例式解读小学分册》",
}

# 缓存已加载的书籍文本
_books_cache: Dict[str, List[str]] = {}


def _load_book(book_id: str) -> List[str]:
    """加载一本书的文本，按行分割"""
    if book_id in _books_cache:
        return _books_cache[book_id]

    filename = BOOK_FILES.get(book_id)
    if not filename:
        return []

    filepath = os.path.join(RAW_BOOKS_DIR, filename)
    if not os.path.exists(filepath):
        return []

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.read().split("\n")

    _books_cache[book_id] = lines
    return lines


def _extract_page_paragraphs(lines: List[str], center_line: int, context: int = 15) -> str:
    """提取相关段落（去重页码标记）"""
    start = max(0, center_line - context)
    end = min(len(lines), center_line + context + 1)

    paragraphs = []
    for line in lines[start:end]:
        # 跳过页面标记
        if re.match(r"^## Page \d+", line.strip()):
            continue
        if line.strip():
            paragraphs.append(line.strip())

    return "\n".join(paragraphs)


def search_books(
    query: str,
    book_ids: Optional[List[str]] = None,
    max_results: int = 5,
    context_lines: int = 15,
) -> List[Dict]:
    """
    在4本书中搜索相关段落

    Args:
        query: 搜索关键词（空格分隔多个关键词）
        book_ids: 限定搜索的书（默认搜索所有）
        max_results: 最大返回结果数
        context_lines: 上下文行数

    Returns:
        搜索结果列表，每项包含 book_id, book_title, text, relevance_score
    """
    if book_ids is None:
        book_ids = list(BOOK_FILES.keys())

    # 解析关键词
    # 支持空格分隔的多词查询，也支持中文连续字符串（自动按2-4字切分）
    stopwords = {"怎么", "如何", "什么", "为什么", "哪些", "可以", "能够", "应该",
                 "的", "了", "是", "在", "和", "与", "或", "不", "也", "都",
                 "这", "那", "有", "没", "会", "能", "要", "就", "才",
                 "呢", "吧", "吗", "啊", "嘛", "么", "呀", "哈"}

    # 先按空格分词
    raw_keywords = [kw.strip() for kw in query.split() if kw.strip()]

    # 对每个关键词进行处理
    keywords = []
    for kw in raw_keywords:
        if len(kw) <= 4:
            if kw not in stopwords and len(kw) >= 2:
                keywords.append(kw)
        else:
            # 长字符串：提取所有2-4字的有意义子串
            # 优先提取4字、3字、2字子串，最多6个
            subs = set()
            for length in [4, 3, 2]:
                for start in range(0, len(kw) - length + 1):
                    sub = kw[start:start+length]
                    if sub not in stopwords and len(sub) >= 2:
                        subs.add(sub)
            # 只保留最有代表性的（前6个）
            keywords.extend(list(subs)[:6])

    if not keywords:
        return []

    # 去重
    keywords = list(dict.fromkeys(keywords))
    if not keywords:
        return []

    results = []

    for book_id in book_ids:
        lines = _load_book(book_id)
        if not lines:
            continue

        for i, line in enumerate(lines):
            line_stripped = line.strip()
            if not line_stripped or len(line_stripped) < 5:
                continue

            # 计算关键词匹配度
            matches = sum(1 for kw in keywords if kw in line_stripped)
            if matches == 0:
                continue

            # 相关性评分：匹配关键词数 × 匹配密度
            score = matches * (matches / len(keywords))

            # 提取上下文段落
            text = _extract_page_paragraphs(lines, i, context_lines)
            if len(text) < 20:
                continue

            results.append({
                "book_id": book_id,
                "book_title": BOOK_TITLES[book_id],
                "text": text[:500],  # 限制长度
                "relevance_score": round(score, 2),
                "keywords_matched": matches,
            })

    # 去重（相似段落只保留最高分）
    seen_texts = set()
    unique_results = []
    for r in sorted(results, key=lambda x: -x["relevance_score"]):
        text_key = r["text"][:100]
        if text_key not in seen_texts:
            seen_texts.add(text_key)
            unique_results.append(r)

    return unique_results[:max_results]


def get_context_for_query(user_message: str, max_chars: int = 2000) -> str:
    """
    根据用户消息，搜索4本书获取相关上下文

    用于注入到系统提示词中，增强回答的准确性

    Args:
        user_message: 用户的提问内容
        max_chars: 最大返回字符数

    Returns:
        格式化的上下文字符串
    """
    # 根据用户消息推断应该优先搜索哪本书
    book_priority = []

    # 学段识别
    if any(kw in user_message for kw in ["小学", "三年级", "四年级", "五年级", "六年级"]):
        book_priority.append("case_primary")

    # 话题识别
    if any(kw in user_message for kw in ["任务", "任务型", "任务链", "前任务", "任务环"]):
        book_priority.append("tblt")
    if any(kw in user_message for kw in ["核心素养", "多元目标", "三目标", "思维品质"]):
        book_priority.extend(["bfee1", "bfee2"])
    if any(kw in user_message for kw in ["教材", "评价", "教研", "反思", "教师发展"]):
        book_priority.append("bfee2")
    if any(kw in user_message for kw in ["语块", "词汇", "语法"]):
        book_priority.extend(["tblt", "bfee1"])
    if any(kw in user_message for kw in ["案例", "课例", "教学设计", "教案"]):
        book_priority.extend(["case_primary", "tblt"])

    # 去重保持顺序，确保所有书都被搜索
    seen = set()
    ordered_books = []
    for b in book_priority:
        if b not in seen:
            seen.add(b)
            ordered_books.append(b)
    # 添加未在优先列表中的书（确保搜索覆盖所有书）
    for b in BOOK_FILES:
        if b not in seen:
            ordered_books.append(b)

    # 搜索
    results = search_books(
        user_message,
        book_ids=ordered_books if ordered_books else None,
        max_results=4,
        context_lines=12,
    )

    if not results:
        return ""

    # 格式化输出
    context_parts = []
    total_chars = 0

    for r in results:
        part = f"【{r['book_title']}】\n{r['text']}\n"
        if total_chars + len(part) > max_chars:
            break
        context_parts.append(part)
        total_chars += len(part)

    if not context_parts:
        return ""

    return "📚 以下是从龚亚夫老师著作中检索到的相关内容：\n\n" + "\n---\n".join(context_parts)


def get_book_toc(book_id: str) -> List[Dict]:
    """获取一本书的目录结构"""
    lines = _load_book(book_id)
    if not lines:
        return []

    toc = []
    in_toc = False
    for line in lines:
        line = line.strip()
        if "目录" in line and len(line) < 10:
            in_toc = True
            continue
        if in_toc:
            if re.match(r"第[一二三四五六七八九十]+章", line):
                toc.append({"level": 1, "title": line})
            elif re.match(r"\d+\.\d+", line):
                toc.append({"level": 2, "title": line})
            elif "前言" in line or "引子" in line:
                toc.append({"level": 1, "title": line})
            # 结束目录
            if len(toc) > 0 and line.startswith("## Page") and "目录" not in line:
                break

    return toc


# 预加载常用搜索索引
def warm_up():
    """预加载所有书籍"""
    for book_id in BOOK_FILES:
        _load_book(book_id)
