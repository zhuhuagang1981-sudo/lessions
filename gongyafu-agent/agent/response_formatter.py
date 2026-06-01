"""
龚亚夫智能体 - 响应格式化
统一响应格式，附加元信息（5本书版本）
"""

from typing import Optional, Dict, Any, List


def format_response(
    reply: str,
    session_id: str,
    is_on_topic: bool = True,
    dialogue_stage: str = "listening",
    probing_count: int = 0,
    goal_dimension: Optional[str] = None,
    grade_level: Optional[str] = None,
    source_books: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """格式化API响应"""
    return {
        "reply": reply,
        "session_id": session_id,
        "is_on_topic": is_on_topic,
        "dialogue_stage": dialogue_stage,
        "probing_count": probing_count,
        "goal_dimension": goal_dimension,
        "grade_level": grade_level,
        "source_books": source_books or [],
    }
