"""
龚亚夫教学智能体
"""

from .system_prompt import SYSTEM_PROMPT, OFF_TOPIC_PROMPT, PROBE_DECISION_PROMPT
from .knowledge_base import KNOWLEDGE_BASE
from .boundary_guard import is_teaching_related, get_redirection_message
from .dialogue_engine import DialogueEngine, DialogueStage
from .response_formatter import format_response

__all__ = [
    "SYSTEM_PROMPT",
    "OFF_TOPIC_PROMPT", 
    "PROBE_DECISION_PROMPT",
    "KNOWLEDGE_BASE",
    "is_teaching_related",
    "get_redirection_message",
    "DialogueEngine",
    "DialogueStage",
    "format_response",
]
