"""
龚亚夫智能体 - 苏格拉底式对话引擎
管理对话状态、追问策略、适时点拨
"""

from enum import Enum
from typing import Optional


class DialogueStage(Enum):
    """对话阶段"""
    INIT = "init"              # 初始阶段，等待第一个问题
    LISTENING = "listening"    # 倾听教师表述
    PROBING_L1 = "probing_l1"  # L1诊断性追问
    PROBING_L2 = "probing_l2"  # L2深入性追问
    PROBING_L3 = "probing_l3"  # L3迁移性追问
    SCAFFOLDING = "scaffolding" # 给予点拨提示
    CONFIRMING = "confirming"  # 确认理解
    COMPLETE = "complete"       # 话题完成


class DialogueEngine:
    """苏格拉底式对话引擎"""
    
    def __init__(self, max_probing_rounds: int = 3, min_probing_rounds: int = 1):
        self.max_probing_rounds = max_probing_rounds
        self.min_probing_rounds = min_probing_rounds
    
    def get_next_stage(self, current_stage: DialogueStage, 
                       probing_count: int, 
                       teacher_response_length: int = 0) -> DialogueStage:
        """
        决定下一步对话阶段
        
        Args:
            current_stage: 当前阶段
            probing_count: 已追问轮数
            teacher_response_length: 教师回复长度（字符数）
        """
        if current_stage == DialogueStage.INIT:
            return DialogueStage.LISTENING
        
        if current_stage == DialogueStage.LISTENING:
            # 教师提出了问题，开始L1追问
            return DialogueStage.PROBING_L1
        
        if current_stage == DialogueStage.PROBING_L1:
            if probing_count < self.min_probing_rounds:
                return DialogueStage.PROBING_L2
            if probing_count >= self.max_probing_rounds:
                return DialogueStage.SCAFFOLDING
            # 教师回复较长说明在深入思考，继续追问
            if teacher_response_length > 100:
                return DialogueStage.PROBING_L2
            return DialogueStage.PROBING_L2
        
        if current_stage == DialogueStage.PROBING_L2:
            if probing_count >= self.max_probing_rounds:
                return DialogueStage.SCAFFOLDING
            return DialogueStage.PROBING_L3
        
        if current_stage == DialogueStage.PROBING_L3:
            return DialogueStage.CONFIRMING
        
        if current_stage == DialogueStage.SCAFFOLDING:
            return DialogueStage.CONFIRMING
        
        if current_stage == DialogueStage.CONFIRMING:
            return DialogueStage.COMPLETE
        
        return DialogueStage.LISTENING
    
    def get_stage_instruction(self, stage: DialogueStage) -> str:
        """获取当前对话阶段的指令补充"""
        instructions = {
            DialogueStage.INIT: (
                "用简短温暖的问候开始，让老师知道你可以帮助他/她探索英语教学理念。"
                "可以说类似：'老师您好，我是龚亚夫教学智能体，可以帮助您理解任务型语言教学和多元目标英语课程理念。"
                "您在教学中有什么困惑吗？'"
            ),
            DialogueStage.LISTENING: (
                "认真倾听老师的问题，识别核心关切。"
                "判断这个问题属于九维度中的哪个/些维度。"
                "然后提出第一个L1诊断性追问，引导老师看到自己可能忽略的维度。"
            ),
            DialogueStage.PROBING_L1: (
                "这是L1诊断性追问阶段。你的目标是帮助老师看到自己思考中的空白。"
                "追问策略：'你提到了XX，那YY呢？'——引导老师注意到未覆盖的维度。"
                "例如：'你关注了语言知识的传授，那学生在思维上会有什么发展呢？'"
            ),
            DialogueStage.PROBING_L2: (
                "这是L2深入性追问阶段。你的目标是检验老师教学设计的逻辑链。"
                "追问策略：'你说的XX和YY之间，学生需要什么桥梁？'——检验逻辑连贯性。"
                "例如：'从能说月份词汇到能描述生日习俗之间，学生还需要什么支持？'"
            ),
            DialogueStage.PROBING_L3: (
                "这是L3迁移性追问阶段。你的目标是帮助老师将理解内化并迁移。"
                "追问策略：'如果换一个单元，你会怎么用这个思路？'——引导方法论内化。"
                "例如：'如果你用同样的语块分类法去处理另一个单元的阅读材料，你会怎么做？'"
            ),
            DialogueStage.SCAFFOLDING: (
                "老师已经思考了几轮但仍未抵达结论，现在给予点拨。"
                "步骤：1. 先肯定老师的思考方向 2. 给出关键提示 3. 引导老师用自己的话总结。"
                "例如：'老师您思考的方向很对。其实这里有一个关键的桥梁——语块的功能分类。"
                "您试试用六类功能去重新审视这个单元的语块，看看会怎样？'"
            ),
            DialogueStage.CONFIRMING: (
                "引导老师总结自己的收获。"
                "例如：'用你自己的话说说，今天我们讨论后，你对XX有了什么新的理解？'"
                "如果老师总结准确，给予肯定。如果有偏差，温和地补充。"
            ),
            DialogueStage.COMPLETE: (
                "话题讨论完成。感谢老师的思考，并自然引导到下一个话题。"
                "例如：'很好的总结！这个理解对您后续的备课会很有帮助。"
                "您还有其他教学方面的困惑吗？'"
            ),
        }
        return instructions.get(stage, "")
    
    def should_probe_or_answer(self, probing_count: int, 
                                teacher_showing_understanding: bool = False) -> str:
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
