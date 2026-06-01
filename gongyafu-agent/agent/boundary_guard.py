"""
龚亚夫智能体 - 话题边界守卫
判断用户输入是否与英语教学相关（5本书版本）
扩展话题范围，增加学段识别
"""

import re
from typing import Optional, Tuple


# 教学相关关键词（高权重）- 扩展至5本书覆盖范围
TEACHING_KEYWORDS = [
    # 教学方法
    "教学", "教案", "备课", "上课", "说课", "评课", "磨课", "反思",
    "任务型", "语块", "句型", "任务链", "读写", "支架", "分层",
    "课堂", "活动设计", "教学设计", "单元设计", "课时",
    # 课程标准
    "课标", "核心素养", "英语学习活动观", "学业质量", "课程内容",
    # 教学评价
    "评价", "量表", "检查", "测试", "作业", "反馈", "形成性",
    "嵌入式评价", "表现性评价",
    # 教师发展
    "教研", "专业发展", "培训", "公开课", "职称", "校本教研",
    "课堂观察", "主题研究",
    # 语言教学
    "英语", "词汇", "语法", "阅读", "写作", "听力", "口语",
    "phonics", "reading", "writing", "speaking", "listening",
    "vocabulary", "grammar", "lesson", "task", "scaffolding",
    # 龚亚夫专有术语
    "多元目标", "社会文化", "思维认知", "语言交流",
    "三个世界", "功能语块", "五步闭环", "三目标",
    # 教材
    "教材", "人教版", "外研版", "课文", "单元", "Section",
    # 新增：5本书扩展话题
    "教材评价", "教材分析", "课程资源", "资源开发",
    "教师成长", "教师反思", "教学决策", "课堂管理",
    "思维层次", "思维品质", "高阶思维", "低阶思维",
    "成长型思维", "元认知",
    "单元整体", "读写结合", "语法教学",
    "文化意识", "文化比较", "国际意识",
    "学科融合", "跨学科",
    "行为规范", "伦理美德",
    # 学段标识
    "小学", "初中", "低年级", "高年级",
    "三年级", "四年级", "五年级", "六年级",
    "七年级", "八年级", "九年级",
    "初一", "初二", "初三",
    "PEP", "Go for it",
]

# 明确非教学关键词
OFF_TOPIC_KEYWORDS = [
    "股票", "基金", "投资", "买房", "贷款",
    "减肥", "美容", "化妆", "穿搭",
    "游戏", "追剧", "综艺", "明星", "电影",
    "做菜", "菜谱", "旅游攻略",
    "修电脑", "手机", "数码",
    "算命", "星座", "风水",
    "法律", "打官司",
    "赌博", "彩票",
    "宠物", "养花",
]

# 模糊领域（可能与教学有关，需进一步判断）
AMBIGUOUS_KEYWORDS = [
    "学生", "管理", "家长", "学校",  # 可能指学生管理，也可能是教学相关
    "考试",  # 可能是教学评价，也可能是非教学考试
    "心理",  # 可能是学生心理（教学相关），也可能是心理咨询
]


def detect_grade_level(message: str) -> Tuple[Optional[str], float]:
    """
    从教师消息中识别学段。

    Returns:
        (grade_level, confidence)
        grade_level: "primary" / "junior" / None
        confidence: 0.0-1.0
    """
    PRIMARY_KEYWORDS = [
        "小学", "低年级", "三年级", "四年级", "五年级", "六年级",
        "小朋友", "孩子", "phonics", "绘本",
        "PEP", "Let's learn", "Let's talk",
        "字母", "自然拼读",
    ]
    JUNIOR_KEYWORDS = [
        "初中", "七年级", "八年级", "九年级",
        "初一", "初二", "初三",
        "中考", "完形填空",
        "Go for it", "Section A", "Section B",
        "语法专项", "写作训练",
    ]

    primary_hits = [kw for kw in PRIMARY_KEYWORDS if kw in message]
    junior_hits = [kw for kw in JUNIOR_KEYWORDS if kw in message]

    if primary_hits and not junior_hits:
        return "primary", min(len(primary_hits) / 3.0, 1.0)
    elif junior_hits and not primary_hits:
        return "junior", min(len(junior_hits) / 3.0, 1.0)
    elif primary_hits and junior_hits:
        if len(primary_hits) > len(junior_hits):
            return "primary", min(len(primary_hits) / 3.0, 1.0)
        else:
            return "junior", min(len(junior_hits) / 3.0, 1.0)
    return None, 0.0


def is_teaching_related(message: str) -> bool:
    """
    判断用户消息是否与英语教学相关。

    5本书版本：话题范围比3本书更广，包括教材评价、
    教师专业发展、校本教研、课堂观察等。

    返回 True 表示相关，False 表示不相关。
    """
    msg_lower = message.lower()

    # 1. 检查是否命中明确的非教学关键词
    off_topic_count = sum(1 for kw in OFF_TOPIC_KEYWORDS if kw in message)
    if off_topic_count >= 2:
        return False
    if off_topic_count == 1:
        # 只有一个非教学关键词，检查是否同时有教学关键词
        teaching_count = sum(1 for kw in TEACHING_KEYWORDS if kw in message)
        if teaching_count == 0:
            return False

    # 2. 检查教学相关关键词密度
    teaching_count = sum(1 for kw in TEACHING_KEYWORDS if kw in message)

    # 3. 检查是否包含教学相关问题模式
    question_patterns = [
        r"怎么.{0,4}教", r"如何.{0,4}设计", r"如何.{0,4}评价",
        r"怎么.{0,4}备课", r"怎样.{0,4}上", r"如何.{0,4}处理",
        r"有没有.{0,4}方法", r"能不能.{0,4}教",
        r"如何.{0,4}观察", r"怎么.{0,4}反思",  # 新增：5本书扩展
        r"怎么.{0,4}评课", r"如何.{0,4}教研",
        r"如何.{0,4}分析", r"怎么.{0,4}分层",
    ]
    pattern_match = any(re.search(p, message) for p in question_patterns)

    # 4. 综合判断
    if teaching_count >= 2:
        return True
    if teaching_count >= 1 and pattern_match:
        return True
    if pattern_match and off_topic_count == 0:
        return True
    if teaching_count == 0 and off_topic_count == 0 and not pattern_match:
        # 完全没有教学关键词，也没有明确非教学关键词
        # 需要进一步判断——默认给通过，让LLM自己判断
        return True

    return teaching_count > 0


def get_grade_specific_redirection(grade_level: Optional[str]) -> str:
    """获取学段特定的引导消息"""
    if grade_level == "primary":
        return "老师，我专注于英语教学领域。作为小学英语老师，您最近在教学中有什么困惑吗？比如活动设计、评价方式、核心素养落地这些方面？"
    elif grade_level == "junior":
        return "老师，我专注于英语教学领域。作为初中英语老师，您最近在教学中有什么困惑吗？比如单元整体教学、读写结合、分层教学这些方面？"
    return ""


def get_redirection_message(message: str = "") -> str:
    """获取话题引导消息，支持学段感知"""
    grade_level, _ = detect_grade_level(message) if message else (None, 0.0)
    grade_redirect = get_grade_specific_redirection(grade_level)
    if grade_redirect:
        return grade_redirect
    return "老师，我专注于英语教学领域，这个问题超出了我的范围。让我帮您想想教学中有没有类似的思考——您在英语教学中有什么困惑吗？"


def get_topic_classification(message: str) -> str:
    """
    对话题进行分类：allowed / borderline / forbidden

    Returns:
        "allowed" - 允许的话题，直接回答
        "borderline" - 边界话题，引导回归
        "forbidden" - 禁止话题，温和拒绝
    """
    # 检查禁止话题
    off_topic_count = sum(1 for kw in OFF_TOPIC_KEYWORDS if kw in message)
    teaching_count = sum(1 for kw in TEACHING_KEYWORDS if kw in message)

    if off_topic_count >= 1 and teaching_count == 0:
        return "forbidden"

    # 检查边界话题（模糊领域但无明确教学关键词）
    ambiguous_hits = [kw for kw in AMBIGUOUS_KEYWORDS if kw in message]
    if ambiguous_hits and teaching_count == 0 and off_topic_count == 0:
        return "borderline"

    # 非英语学科教学（有教学关键词但明确不是英语）
    non_english_subject = ["数学", "语文", "物理", "化学", "生物", "历史", "地理", "政治", "体育", "音乐", "美术"]
    if any(s in message for s in non_english_subject) and "英语" not in message:
        return "borderline"

    return "allowed"
