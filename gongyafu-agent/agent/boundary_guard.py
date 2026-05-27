"""
龚亚夫智能体 - 话题边界守卫
判断用户输入是否与英语教学相关
"""

import re

# 教学相关关键词（高权重）
TEACHING_KEYWORDS = [
    # 教学方法
    "教学", "教案", "备课", "上课", "说课", "评课", "磨课", "反思",
    "任务型", "语块", "句型", "任务链", "读写", "支架", "分层",
    "课堂", "活动设计", "教学设计", "单元设计", "课时",
    # 课程标准
    "课标", "核心素养", "英语学习活动观", "学业质量", "课程内容",
    # 教学评价
    "评价", "量表", "检查", "测试", "作业", "反馈",
    # 教师发展
    "教研", "专业发展", "培训", "公开课", "职称",
    # 语言教学
    "英语", "词汇", "语法", "阅读", "写作", "听力", "口语",
    "phonics", "reading", "writing", "speaking", "listening",
    "vocabulary", "grammar", "lesson", "task", "scaffolding",
    # 龚亚夫专有术语
    "多元目标", "社会文化", "思维认知", "语言交流",
    "三个世界", "功能语块", "五步闭环",
    # 教材
    "教材", "人教版", "外研版", "课文", "单元", "Section",
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
]

# 模糊领域（可能与教学有关，需进一步判断）
AMBIGUOUS_KEYWORDS = [
    "学生", "管理", "家长", "学校",  # 可能指学生管理，也可能是教学相关
]


def is_teaching_related(message: str) -> bool:
    """
    判断用户消息是否与英语教学相关。
    
    使用规则匹配 + 关键词密度判断。
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


def get_redirection_message() -> str:
    """获取话题引导消息"""
    return "老师，我专注于英语教学领域，这个问题超出了我的范围。让我帮您想想教学中有没有类似的思考——您在英语教学中有什么困惑吗？"
