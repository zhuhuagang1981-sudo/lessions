"""
龚亚夫教学智能体
"""

from .system_prompt import SYSTEM_PROMPT, OFF_TOPIC_PROMPT, PROBE_DECISION_PROMPT
from .knowledge_base import KNOWLEDGE_BASE
from .boundary_guard import (
    is_teaching_related,
    get_redirection_message,
    detect_grade_level,
    get_topic_classification,
)
from .dialogue_engine import (
    DialogueEngine,
    DialogueStage,
    SourceTracking,
    CaseGuidance,
    GradeLevelAwareness,
    book_cross_reference,
    BOOK_TASK,
    BOOK_FOUNDATION_1,
    BOOK_FOUNDATION_2,
    BOOK_PRIMARY,
    BOOK_JUNIOR,
    BOOK_NAMES,
)
from .response_formatter import format_response
from .book_search import search_books, get_context_for_query, get_book_toc

__all__ = [
    "SYSTEM_PROMPT",
    "OFF_TOPIC_PROMPT",
    "PROBE_DECISION_PROMPT",
    "KNOWLEDGE_BASE",
    "is_teaching_related",
    "get_redirection_message",
    "detect_grade_level",
    "get_topic_classification",
    "DialogueEngine",
    "DialogueStage",
    "SourceTracking",
    "CaseGuidance",
    "GradeLevelAwareness",
    "book_cross_reference",
    "BOOK_TASK",
    "BOOK_FOUNDATION_1",
    "BOOK_FOUNDATION_2",
    "BOOK_PRIMARY",
    "BOOK_JUNIOR",
    "BOOK_NAMES",
    "format_response",
    "search_books",
    "get_context_for_query",
    "get_book_toc",
]
