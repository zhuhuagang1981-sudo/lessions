"""
龚亚夫智能体 - 苏格拉底式对话引擎
管理对话状态、追问策略、5本书引用追踪、案例引导、学段识别
"""

from enum import Enum
from typing import Optional, List, Dict, Any, Set
from dataclasses import dataclass, field


class DialogueStage(Enum):
    """对话阶段"""
    INIT = "init"              # 初始阶段，等待第一个问题
    LISTENING = "listening"    # 倾听教师表述
    PROBING_L1 = "probing_l1"  # L1诊断性追问
    PROBING_L2 = "probing_l2"  # L2深入性追问 + 案例引导
    PROBING_L3 = "probing_l3"  # L3迁移性追问
    SCAFFOLDING = "scaffolding" # 给予点拨提示
    CONFIRMING = "confirming"  # 确认理解
    COMPLETE = "complete"       # 话题完成


# 五本书编号
BOOK_TASK = "task"          # 《任务型语言教学》
BOOK_FOUNDATION_1 = "foundation_1"  # 《基础外语教育与研究 第一辑》
BOOK_FOUNDATION_2 = "foundation_2"  # 《基础外语教育与研究 第二辑》
BOOK_PRIMARY = "primary"    # 《案例式解读小学分册》
BOOK_JUNIOR = "junior"      # 《案例式解读初中分册》

BOOK_NAMES = {
    BOOK_TASK: "《任务型语言教学》",
    BOOK_FOUNDATION_1: "《基础外语教育与研究 第一辑》",
    BOOK_FOUNDATION_2: "《基础外语教育与研究 第二辑》",
    BOOK_PRIMARY: "《案例式解读小学分册》",
    BOOK_JUNIOR: "《案例式解读初中分册》",
}

# 追问问题库：按5本书分类
PROBE_QUESTIONS: Dict[str, Dict[str, List[str]]] = {
    BOOK_TASK: {
        "L1": [
            "你提到了这个教学活动，那学生在这个活动中要完成的任务是什么？",
            "你关注了语言知识的传授，那学生用这些语言做什么事情呢？",
            "这个活动的目的是操练句型，那学生在什么真实的情境下会用到这个句型？",
            "你设计了这个操练环节，那语言在不同任务中如何自然复现呢？",
        ],
        "L2": [
            "从你说的语言输入到学生能独立完成任务之间，需要什么桥梁？",
            "你提到了语块教学，那这些语块按功能怎么分类？不同功能之间怎么串联？",
            "任务链是从学习理解到迁移创新的，你现在的设计在哪个层次偏多？",
            "我听过一位老师这样上这节课——她先让学生在生活中找出含有这些语块的例子，再设计任务让学生用这些语块去解决问题。你觉得这个思路怎样？",
        ],
        "L3": [
            "如果用同样的语块-句型-任务链方法去处理另一个单元，你会怎么设计？",
            "这个任务型的思路，能不能用到语法教学中？怎么用？",
            "如果换一个完全不同的话题，你的任务链设计会有什么变化？",
        ],
    },
    BOOK_FOUNDATION_1: {
        "L1": [
            "你关注了语言交流目标，那社会文化目标在这个课里怎么体现？",
            "你设计了这个教学活动，那学生的思维能力在这个活动中会有什么发展？",
            "你提到了语言知识教学，那这三个目标——社会文化、思维认知、语言交流，你怎么平衡？",
            "这节课有没有连接学生的'内心世界'？比如让学生表达真实的感受和观点？",
        ],
        "L2": [
            "你说的'培养学生思维能力'具体指什么层次？是识别和记忆，还是分析和评价？",
            "关键不在于教了多少词，而在于学生会不会用这些词去思考——你的设计中，学生有没有真正的思考空间？",
            "我听过一位老师这样上这节课——她在教food词汇时，让学生辩论'学校午餐健不健康'，词汇学习变成了思维训练。你有没有想过类似的设计？",
        ],
        "L3": [
            "如果你用多元目标的框架去审视另一个单元，三个目标分别怎么体现？",
            "这种'语言教学承载思维培养'的思路，在你的日常教学中可以怎么系统化？",
        ],
    },
    BOOK_FOUNDATION_2: {
        "L1": [
            "你选了这个教学活动，那活动设计背后的理念依据是什么？",
            "你提到了教材的使用，那你对这套教材的评价是什么？它适不适合你的学生？",
            "这个课堂活动学生参与度怎么样？你观察过吗？",
        ],
        "L2": [
            "你说的这个教学设计，如果从课堂观察的维度来看——教师提问层次、学生参与方式、语言真实性——哪些方面还有空间？",
            "关键不在于课堂好不好看，而在于学生有没有学——你怎么判断学生真正学到了？",
            "我听过一位老师，她每次课后都用三个问题反思：学生做了什么？学了什么？为什么这样设计？你觉得这个反思框架有用吗？",
        ],
        "L3": [
            "这种教材分析的方法，能不能用到其他单元？你会怎么做？",
            "如果你用课堂观察的框架去听同行的课，你会重点看什么？",
        ],
    },
    BOOK_PRIMARY: {
        "L1": [
            "这个活动设计，小学低年级的孩子能理解吗？他们的认知特点你考虑了吗？",
            "游戏化设计很好，但游戏背后的学习目标是什么？",
            "你的评价方式是什么？小学生能不能看懂评价标准？",
        ],
        "L2": [
            "活动看起来很热闹，但思维的层次在哪里？学生是在识别记忆，还是在分析比较？",
            "关键不在于活动多有趣，而在于活动结束后学生学到了什么——你怎么确保这一点？",
            "我听过一位小学老师，她在教colors的时候不是简单地指物说颜色，而是让学生给教室配色并解释为什么，思维一下子就上去了。你有没有想过类似的设计？",
        ],
        "L3": [
            "这种'游戏+思维'的设计思路，能不能用到其他单元？怎么调整？",
            "如果你的同事也要教这个内容，你会建议她注意什么？",
        ],
    },
    BOOK_JUNIOR: {
        "L1": [
            "你提到了这个教学环节，那它在这个单元整体设计中处于什么位置？",
            "读写结合的课，从读到写之间的桥梁是什么？",
            "语法教学你是怎么处理的？是规则先行还是让学生在语境中发现？",
        ],
        "L2": [
            "单元整体教学的关键不在于'整合'，而在于'有逻辑地整合'——你设计的任务链逻辑线是什么？",
            "从读到写之间有口头内化环节吗？学生先能说，才能写——这个环节你怎么设计？",
            "我听过一位老师教初中写作，她先让学生口头描述自己的周末，再把口头表达转化成书面语，效果特别好。你的读写结合课有没有类似的桥梁？",
        ],
        "L3": [
            "这个单元整体设计的思路，换一个单元你会怎么调整？",
            "分层教学的三层支架设计，在你的课堂上怎么落地？会遇到什么困难？",
        ],
    },
}


@dataclass
class SourceTracking:
    """引用追踪：记录对话中引用了哪本书的哪些知识点"""
    books_referenced: Set[str] = field(default_factory=set)
    topics_by_book: Dict[str, List[str]] = field(default_factory=dict)
    cross_references: List[Dict[str, str]] = field(default_factory=list)

    def add_reference(self, book: str, topic: str):
        """记录一次引用"""
        self.books_referenced.add(book)
        if book not in self.topics_by_book:
            self.topics_by_book[book] = []
        if topic not in self.topics_by_book[book]:
            self.topics_by_book[book].append(topic)

    def add_cross_reference(self, topic: str, books: List[str], note: str = ""):
        """记录跨书交叉引用"""
        self.cross_references.append({
            "topic": topic,
            "books": books,
            "note": note,
        })

    def get_summary(self) -> str:
        """获取引用摘要"""
        if not self.books_referenced:
            return "本次对话尚未引用任何著作。"
        lines = []
        for book in self.books_referenced:
            book_name = BOOK_NAMES.get(book, book)
            topics = self.topics_by_book.get(book, [])
            if topics:
                lines.append(f"- {book_name}：{', '.join(topics)}")
            else:
                lines.append(f"- {book_name}")
        if self.cross_references:
            lines.append("\n跨书关联：")
            for cr in self.cross_references:
                books_str = "、".join(BOOK_NAMES.get(b, b) for b in cr["books"])
                note = f"（{cr['note']}）" if cr["note"] else ""
                lines.append(f"- {cr['topic']}：{books_str}{note}")
        return "\n".join(lines)


@dataclass
class CaseGuidance:
    """案例引导状态"""
    case_used: bool = False          # 是否已使用案例引导
    case_stage: str = ""             # 在哪个阶段使用了案例
    case_topic: str = ""             # 案例涉及的话题
    follow_up_needed: bool = False   # 是否需要跟进案例讨论

    def mark_case_used(self, stage: str, topic: str):
        """标记已使用案例引导"""
        self.case_used = True
        self.case_stage = stage
        self.case_topic = topic

    def should_use_case(self, probing_count: int, stage: DialogueStage) -> bool:
        """判断是否应该使用案例引导"""
        # L2阶段追问效果递减时引入案例
        if stage == DialogueStage.PROBING_L2 and probing_count >= 2 and not self.case_used:
            return True
        # 支架阶段优先用案例而非直接说理
        if stage == DialogueStage.SCAFFOLDING and not self.case_used:
            return True
        return False


@dataclass
class GradeLevelAwareness:
    """学段识别与追踪"""
    detected_level: Optional[str] = None  # "primary" / "junior" / None
    confidence: float = 0.0
    indicators: List[str] = field(default_factory=list)

    # 小学关键词
    PRIMARY_KEYWORDS = [
        "小学", "低年级", "三年级", "四年级", "五年级", "六年级",
        "小朋友", "孩子", "游戏教学", "phonics", "绘本",
        "人教版PEP", "PEP", "Let's learn", "Let's talk",
        "字母", "自然拼读",
    ]
    # 初中关键词
    JUNIOR_KEYWORDS = [
        "初中", "七年级", "八年级", "九年级",
        "初一", "初二", "初三",
        "中考", "阅读理解", "完形填空",
        "人教版Go for it", "Go for it", "Section A", "Section B",
        "语法专项", "写作训练",
    ]

    def detect(self, message: str) -> Optional[str]:
        """从教师消息中识别学段"""
        primary_hits = [kw for kw in self.PRIMARY_KEYWORDS if kw in message]
        junior_hits = [kw for kw in self.JUNIOR_KEYWORDS if kw in message]

        if primary_hits and not junior_hits:
            self.detected_level = "primary"
            self.confidence = min(len(primary_hits) / 3.0, 1.0)
            self.indicators = primary_hits
            return "primary"
        elif junior_hits and not primary_hits:
            self.detected_level = "junior"
            self.confidence = min(len(junior_hits) / 3.0, 1.0)
            self.indicators = junior_hits
            return "junior"
        elif primary_hits and junior_hits:
            # 都命中了，按命中数量判断
            if len(primary_hits) > len(junior_hits):
                self.detected_level = "primary"
                self.indicators = primary_hits
                return "primary"
            else:
                self.detected_level = "junior"
                self.indicators = junior_hits
                return "junior"
        return None

    def get_recommended_book(self) -> str:
        """根据学段推荐对应的案例分册"""
        if self.detected_level == "primary":
            return BOOK_PRIMARY
        elif self.detected_level == "junior":
            return BOOK_JUNIOR
        return BOOK_PRIMARY  # 默认先推荐小学分册

    def get_grade_label(self) -> str:
        """获取学段中文标签"""
        if self.detected_level == "primary":
            return "小学"
        elif self.detected_level == "junior":
            return "初中"
        return ""


def book_cross_reference(topic: str) -> List[Dict[str, Any]]:
    """
    跨书交叉引用：当一个话题在多本书中都有论述时，返回不同角度。

    Returns:
        List of {"book": book_id, "book_name": str, "angle": str}
    """
    CROSS_REF_MAP = {
        "语块教学": [
            {"book": BOOK_TASK, "angle": "语块的功能分类和任务设计方法"},
            {"book": BOOK_FOUNDATION_1, "angle": "语块教学的理论基础——语言交流目标"},
            {"book": BOOK_JUNIOR, "angle": "初中读写结合中的语块提取与运用"},
            {"book": BOOK_PRIMARY, "angle": "小学语块教学的语境化策略"},
        ],
        "思维能力": [
            {"book": BOOK_TASK, "angle": "任务设计与思维层次的对应关系"},
            {"book": BOOK_FOUNDATION_1, "angle": "思维认知目标的理论框架"},
            {"book": BOOK_FOUNDATION_2, "angle": "课堂观察中的思维维度"},
            {"book": BOOK_PRIMARY, "angle": "小学课堂提问的层次设计"},
            {"book": BOOK_JUNIOR, "angle": "初中读写中的思维递进"},
        ],
        "读写结合": [
            {"book": BOOK_TASK, "angle": "任务型教学中的读写任务链"},
            {"book": BOOK_FOUNDATION_1, "angle": "语言技能整合的理论基础"},
            {"book": BOOK_JUNIOR, "angle": "初中读写结合的操作路径"},
        ],
        "评价": [
            {"book": BOOK_TASK, "angle": "任务型教学的评价关注任务完成度"},
            {"book": BOOK_FOUNDATION_1, "angle": "三目标框架下的评价维度"},
            {"book": BOOK_FOUNDATION_2, "angle": "课堂观察与校本教研的评价框架"},
            {"book": BOOK_PRIMARY, "angle": "小学形成性评价的实践策略"},
            {"book": BOOK_JUNIOR, "angle": "初中嵌入式评价与教-学-评一体化"},
        ],
        "分层教学": [
            {"book": BOOK_TASK, "angle": "任务难度六因素与分层设计"},
            {"book": BOOK_JUNIOR, "angle": "初中三层支架的操作方法"},
        ],
        "单元整体教学": [
            {"book": BOOK_TASK, "angle": "任务链设计的递进逻辑"},
            {"book": BOOK_FOUNDATION_1, "angle": "多元目标在单元中的统整"},
            {"book": BOOK_JUNIOR, "angle": "初中单元整体设计的操作框架"},
        ],
        "教材分析": [
            {"book": BOOK_FOUNDATION_1, "angle": "三目标视角下的教材解读"},
            {"book": BOOK_FOUNDATION_2, "angle": "教材评价双维度框架"},
        ],
        "教师发展": [
            {"book": BOOK_FOUNDATION_1, "angle": "教师理念转变是发展的核心"},
            {"book": BOOK_FOUNDATION_2, "angle": "教师成长阶段与反思路径"},
        ],
        "语法教学": [
            {"book": BOOK_TASK, "angle": "语法在任务中的自然呈现"},
            {"book": BOOK_JUNIOR, "angle": "初中语法教学五步路径"},
        ],
        "核心素养": [
            {"book": BOOK_FOUNDATION_1, "angle": "三目标与核心素养四维的映射"},
            {"book": BOOK_PRIMARY, "angle": "小学核心素养落地的策略"},
            {"book": BOOK_JUNIOR, "angle": "初中核心素养在单元中的体现"},
        ],
    }
    return CROSS_REF_MAP.get(topic, [])


class DialogueEngine:
    """苏格拉底式对话引擎（5本书版本）"""

    def __init__(self, max_probing_rounds: int = 3, min_probing_rounds: int = 1):
        self.max_probing_rounds = max_probing_rounds
        self.min_probing_rounds = min_probing_rounds

    def get_next_stage(self, current_stage: DialogueStage,
                       probing_count: int,
                       teacher_response_length: int = 0,
                       case_guidance: Optional[CaseGuidance] = None) -> DialogueStage:
        """
        决定下一步对话阶段

        Args:
            current_stage: 当前阶段
            probing_count: 已追问轮数
            teacher_response_length: 教师回复长度（字符数）
            case_guidance: 案例引导状态
        """
        if current_stage == DialogueStage.INIT:
            return DialogueStage.LISTENING

        if current_stage == DialogueStage.LISTENING:
            return DialogueStage.PROBING_L1

        if current_stage == DialogueStage.PROBING_L1:
            if probing_count < self.min_probing_rounds:
                return DialogueStage.PROBING_L2
            if probing_count >= self.max_probing_rounds:
                return DialogueStage.SCAFFOLDING
            return DialogueStage.PROBING_L2

        if current_stage == DialogueStage.PROBING_L2:
            if probing_count >= self.max_probing_rounds:
                return DialogueStage.SCAFFOLDING
            # 如果已经在L2阶段使用了案例引导，继续推进到L3
            if case_guidance and case_guidance.case_used:
                return DialogueStage.PROBING_L3
            return DialogueStage.PROBING_L3

        if current_stage == DialogueStage.PROBING_L3:
            return DialogueStage.CONFIRMING

        if current_stage == DialogueStage.SCAFFOLDING:
            return DialogueStage.CONFIRMING

        if current_stage == DialogueStage.CONFIRMING:
            return DialogueStage.COMPLETE

        return DialogueStage.LISTENING

    def get_stage_instruction(self, stage: DialogueStage,
                               grade_level: Optional[str] = None,
                               source_tracking: Optional[SourceTracking] = None,
                               case_guidance: Optional[CaseGuidance] = None) -> str:
        """
        获取当前对话阶段的指令补充

        Args:
            stage: 对话阶段
            grade_level: 检测到的学段 ("primary"/"junior"/None)
            source_tracking: 引用追踪状态
            case_guidance: 案例引导状态
        """
        grade_note = ""
        if grade_level == "primary":
            grade_note = "（教师关注小学教学，优先引用小学分册案例）"
        elif grade_level == "junior":
            grade_note = "（教师关注初中教学，优先引用初中分册案例）"

        source_note = ""
        if source_tracking and source_tracking.books_referenced:
            books_str = "、".join(BOOK_NAMES.get(b, b) for b in source_tracking.books_referenced)
            source_note = f"\n已引用著作：{books_str}。注意补充未引用著作的相关视角。"

        instructions = {
            DialogueStage.INIT: (
                "用简短温暖的问候开始，像龚亚夫老师本人一样自然。"
                "可以说类似：'老师您好，有什么教学上的想法想聊聊？'"
                "不说'我是AI助手'，自然地进入角色。"
            ),
            DialogueStage.LISTENING: (
                "认真倾听老师的问题，识别核心关切。"
                "判断这个问题属于九维度中的哪个/些维度。"
                f"识别教师提到的学段{grade_note}。"
                "然后提出第一个L1诊断性追问，引导老师看到自己可能忽略的维度。"
                "风格提示：用'你有没有想过...'或'如果我们换一个角度...'开头。"
            ),
            DialogueStage.PROBING_L1: (
                "这是L1诊断性追问阶段。帮助老师看到自己思考中的空白。"
                "追问策略：'你提到了XX，那YY呢？'——引导老师注意到未覆盖的维度。"
                f"{grade_note}"
                "风格提示：先肯定老师提到的部分，再用'关键不在于XX，而在于YY'推进。"
                "例如：'你关注了语言知识的传授，关键不在于教了多少词，而在于学生会不会用——"
                "那学生在这个活动中思维上会有什么发展呢？'"
            ),
            DialogueStage.PROBING_L2: (
                "这是L2深入性追问阶段。检验老师教学设计的逻辑链，适时引入案例引导。"
                "追问策略：'你说的XX和YY之间，学生需要什么桥梁？'——检验逻辑连贯性。"
                f"{grade_note}"
                "案例引导策略：如果追问效果递减，用'我听过一位老师这样上这节课...'引入案例，"
                "用具体教学场景帮助老师理解，而非直接说理。"
                "风格提示：用反问推进——'但是，这样教的话，学生的思维发展在哪里呢？'"
                "例如：'从能说月份词汇到能描述生日习俗之间，学生还需要什么支持？"
                "我听过一位老师，她让学生用月份词讨论自己的生日计划，词汇一下子活了起来。'"
            ),
            DialogueStage.PROBING_L3: (
                "这是L3迁移性追问阶段。帮助老师将理解内化并迁移。"
                "追问策略：'如果换一个单元，你会怎么用这个思路？'——引导方法论内化。"
                f"{grade_note}"
                "风格提示：用'你说得对，不过还有一层——'推进，引导深度思考。"
                "例如：'如果你用同样的语块分类法去处理另一个单元的阅读材料，你会怎么做？'"
            ),
            DialogueStage.SCAFFOLDING: (
                "老师已经思考了几轮但仍未抵达结论，现在给予点拨。"
                "优先使用案例引导而非直接说理——'我听过一位老师这样上这节课...'"
                "步骤：1. 先肯定老师的思考方向 2. 用案例或比喻给出关键提示 3. 引导老师用自己的话总结。"
                f"{grade_note}"
                "风格提示：用'其实，我们还可以这样想...'引入新视角。"
                "例如：'老师您思考的方向很对。其实，这里有一个关键的桥梁——语块的功能分类。"
                "我听过一位老师用六类功能去重新审视单元语块，一下子就把读写打通了。您试试看？'"
            ),
            DialogueStage.CONFIRMING: (
                "引导老师总结自己的收获。"
                "例如：'用你自己的话说说，今天我们讨论后，你对XX有了什么新的理解？'"
                "如果老师总结准确，给予肯定。如果有偏差，温和地补充。"
                "风格提示：简洁确认，不说空洞的'非常好'，而是具体指出老师理解到了哪个层次。"
            ),
            DialogueStage.COMPLETE: (
                "话题讨论完成。感谢老师的思考，并自然引导到下一个话题。"
                "例如：'很好的总结！这个理解对你后续备课会有帮助。"
                "你还有其他教学方面的困惑吗？'"
                "风格提示：简短有力，不说废话。"
            ),
        }
        instruction = instructions.get(stage, "")
        if source_note:
            instruction += source_note
        return instruction

    def should_probe_or_answer(self, probing_count: int,
                                teacher_showing_understanding: bool = False,
                                case_guidance: Optional[CaseGuidance] = None) -> str:
        """
        判断应该继续追问还是直接回答
        返回 'probe', 'scaffold', 或 'answer'
        """
        if teacher_showing_understanding and probing_count >= self.min_probing_rounds:
            return 'answer'
        if probing_count >= self.max_probing_rounds:
            return 'scaffold'
        if probing_count < self.min_probing_rounds:
            return 'probe'
        return 'probe'

    def get_probe_question(self, book: str, level: str) -> Optional[str]:
        """获取指定书和层次的追问问题"""
        questions = PROBE_QUESTIONS.get(book, {}).get(level, [])
        if not questions:
            return None
        # 简单轮询，实际应用中可以根据上下文选择最合适的问题
        import random
        return random.choice(questions)

    def get_probe_questions_by_grade(self, grade_level: Optional[str],
                                      level: str,
                                      fallback_book: str = BOOK_TASK) -> List[str]:
        """
        根据学段获取追问问题

        Args:
            grade_level: 学段 ("primary"/"junior"/None)
            level: 追问层次 ("L1"/"L2"/"L3")
            fallback_book: 无学段时的默认书
        """
        questions = []
        # 始终包含任务型教学的问题
        task_qs = PROBE_QUESTIONS.get(BOOK_TASK, {}).get(level, [])
        if task_qs:
            questions.extend(task_qs)

        # 根据学段添加分册问题
        if grade_level == "primary":
            primary_qs = PROBE_QUESTIONS.get(BOOK_PRIMARY, {}).get(level, [])
            questions.extend(primary_qs)
        elif grade_level == "junior":
            junior_qs = PROBE_QUESTIONS.get(BOOK_JUNIOR, {}).get(level, [])
            questions.extend(junior_qs)
        else:
            # 没有学段信息，两个分册都加
            primary_qs = PROBE_QUESTIONS.get(BOOK_PRIMARY, {}).get(level, [])
            junior_qs = PROBE_QUESTIONS.get(BOOK_JUNIOR, {}).get(level, [])
            questions.extend(primary_qs)
            questions.extend(junior_qs)

        return questions
