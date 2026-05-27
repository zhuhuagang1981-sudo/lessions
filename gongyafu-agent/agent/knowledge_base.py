"""
龚亚夫智能体 - 结构化知识库
基于三本著作的完整知识体系
"""

KNOWLEDGE_BASE = {
    "meta": {
        "name": "龚亚夫教学理念知识库",
        "version": "1.0",
        "sources": [
            "《英语教育新论：多元目标英语课程》（高等教育出版社，2015）",
            "《任务型语言教学》修订版（人民教育出版社，2006）",
            "《义务教育英语课程标准（2022年版）案例式解读》（华东师大出版社，2023）"
        ],
        "constraint": "本知识库仅包含龚亚夫老师三本著作的教学理念，不包含其他来源"
    },

    "core_frameworks": {
        "three_goals": {
            "name": "多元目标英语课程",
            "description": "英语教育应实现三大目标，三者密不可分",
            "goals": {
                "social_cultural": {
                    "name": "社会文化目标",
                    "description": "通过英语教育培养学生的社会文化素养",
                    "sub_dimensions": {
                        "ethics_virtues": {
                            "name": "行为规范与伦理美德",
                            "description": "通过英语学习培养礼貌、诚信、尊重、合作等品质",
                            "examples": [
                                "学习'Please''Thank you''Excuse me'等不仅是语言，更是行为规范教育",
                                "小组合作任务培养团队精神和责任感",
                                "阅读关于诚信的故事，讨论'What would you do?'培养判断力"
                            ],
                            "teaching_implications": "语言材料的选择和任务设计应体现正面价值观引导"
                        },
                        "social_knowledge_integration": {
                            "name": "社会知识与学科融合",
                            "description": "英语不是孤立学科，与历史、地理、科学等学科相连",
                            "examples": [
                                "学习食物词汇时融入营养学知识",
                                "学习天气表达时结合地理知识",
                                "阅读环保话题文章时整合科学和公民教育"
                            ],
                            "teaching_implications": "选择跨学科主题的内容，设计需要调用多学科知识的任务"
                        },
                        "multicultural_international": {
                            "name": "多元文化与国际意识",
                            "description": "理解不同文化，形成开放的国际视野",
                            "examples": [
                                "比较中西方节日习俗，理解文化差异",
                                "讨论全球性问题（环保、和平），培养国际意识",
                                "阅读不同国家学生的日常生活，增进理解"
                            ],
                            "teaching_implications": "不只教'外国文化是什么'，更要引导'为什么不同'和'如何理解'"
                        }
                    }
                },
                "cognitive_thinking": {
                    "name": "思维认知目标",
                    "description": "培养思维能力和学习策略",
                    "sub_dimensions": {
                        "growth_mindset": {
                            "name": "积极心理品质（成长型思维）",
                            "description": "相信自己能通过努力提升，不怕犯错",
                            "examples": [
                                "鼓励学生'I can try'而非'I can't'",
                                "将错误视为学习机会而非失败",
                                "设计有挑战但可达成的任务，让学生体验成功"
                            ],
                            "teaching_implications": "评价方式应关注进步而非仅看结果，营造安全的错误表达环境"
                        },
                        "thinking_levels": {
                            "name": "多层次思维能力",
                            "description": "从识别描述到分析比较再到评价创造",
                            "levels": [
                                {"level": "低阶思维", "skills": ["识别", "回忆", "描述", "理解"], "question_types": ["What", "Who", "When", "Where"]},
                                {"level": "中阶思维", "skills": ["分析", "比较", "分类", "推断"], "question_types": ["How", "Why", "Compare", "What if"]},
                                {"level": "高阶思维", "skills": ["评价", "论证", "创造", "反思"], "question_types": ["Evaluate", "Argue", "Design", "Create"]}
                            ],
                            "teaching_implications": "每节课都应有不同思维层次的活动，不能停留在低阶"
                        },
                        "learning_strategies": {
                            "name": "有效学习策略",
                            "description": "元认知策略、资源策略、交际策略",
                            "examples": [
                                "元认知策略：让学生制定学习计划、自我监控、反思调整",
                                "资源策略：教会学生使用词典、网络资源、同伴资源",
                                "交际策略：教学生如何澄清、如何请求帮助、如何维持对话"
                            ],
                            "teaching_implications": "不只是教知识，更要教'如何学'"
                        }
                    }
                },
                "language_communication": {
                    "name": "语言交流目标",
                    "description": "掌握语言知识和技能，实现有效交流",
                    "sub_dimensions": {
                        "language_knowledge": {
                            "name": "基本语言知识",
                            "description": "语音、词汇、语法、语篇",
                            "key_points": [
                                "词汇教学应通过语块而非孤立单词",
                                "语法教学应在语境中自然呈现而非规则先行",
                                "语篇意识比句子层面的准确性更重要"
                            ]
                        },
                        "language_skills": {
                            "name": "基本语言技能",
                            "description": "听、说、读、看、写",
                            "key_points": [
                                "技能不应孤立训练，在任务中整合使用",
                                "读写结合是核心路径：读为输入、写为输出",
                                "'看'（viewing）是2022版课标新增的技能维度"
                            ]
                        },
                        "communication_strategies": {
                            "name": "交流沟通策略",
                            "description": "如何得体地表达、如何理解言外之意",
                            "examples": [
                                "学会在不同场合选择合适的表达方式",
                                "理解间接表达的含义（如'It's a bit cold here'可能是请求关窗）",
                                "在交际困难时使用补偿策略（解释、手势、替换词）"
                            ]
                        }
                    }
                }
            },
            "key_principle": "三大目标密不可分——语言教学本身就承载着社会文化和思维认知的培养使命，不能只教语言"
        },

        "three_worlds": {
            "name": "三个世界理论",
            "description": "中国学生生活在三个世界中，英语教学应连接三个世界",
            "worlds": {
                "inner_world": {
                    "name": "内心世界",
                    "description": "情感、态度、价值观、自我认知",
                    "teaching_connection": "选择能触动学生内心的材料，设计让学生表达真实感受的活动"
                },
                "knowledge_world": {
                    "name": "知识世界",
                    "description": "学科知识、社会常识、文化理解",
                    "teaching_connection": "语言教学不只是语言知识，还承载着文化知识和社会常识"
                },
                "future_world": {
                    "name": "未来世界",
                    "description": "理想、规划、国际视野、社会责任",
                    "teaching_connection": "设计展望未来的任务，培养国际视野和社会责任感"
                }
            }
        },

        "task_based": {
            "name": "任务型语言教学",
            "description": "以'做事情'为驱动的语言教学方式",
            "six_principles": [
                {
                    "name": "以任务为主线",
                    "description": "教学围绕有意义的任务展开，而非围绕语言点",
                    "traditional_vs_task": "传统教学从语言形式出发，任务型教学从意义和任务出发"
                },
                {
                    "name": "以培养思维能力为目标",
                    "description": "任务设计要促进学生的分析、比较、评价等思维活动",
                    "traditional_vs_task": "传统教学侧重识别和记忆，任务型教学促进分析评价创造"
                },
                {
                    "name": "激发兴趣动力",
                    "description": "任务要贴近学生生活，激发参与动机",
                    "traditional_vs_task": "传统教学靠外在奖惩驱动，任务型教学靠任务本身的意义驱动"
                },
                {
                    "name": "语言不断复现",
                    "description": "核心语言在不同任务中反复出现，加深记忆",
                    "traditional_vs_task": "传统教学依赖记忆练习，任务型教学在不同任务中自然复现"
                },
                {
                    "name": "语境真实性",
                    "description": "任务情境要模拟真实交际场景",
                    "traditional_vs_task": "传统教学为练句型设计场景，任务型教学从真实场景出发设计任务"
                },
                {
                    "name": "核心素养全面内涵",
                    "description": "不只是语言能力，还有文化意识和思维品质",
                    "traditional_vs_task": "传统教学关注语言准确性，任务型教学关注任务完成度和综合素养"
                }
            ],
            "classic_cases": [
                {
                    "name": "打喷嚏卫生礼貌",
                    "description": "从日常行为切入，讨论不同文化的礼貌表达",
                    "goal_dimension": "社会文化目标+语言交流目标"
                },
                {
                    "name": "判断好朋友",
                    "description": "用英语讨论友情标准，训练评价和论证思维",
                    "goal_dimension": "思维认知目标+语言交流目标"
                },
                {
                    "name": "帮奶奶找公交卡",
                    "description": "模拟真实问题解决场景",
                    "goal_dimension": "语言交流目标+思维认知目标"
                },
                {
                    "name": "Jimmy日常作息",
                    "description": "从个人信息出发，拓展到生活习惯比较",
                    "goal_dimension": "三目标融合"
                }
            ]
        },

        "chunk_pattern_task": {
            "name": "语块—句型—任务链",
            "description": "龚亚夫任务型教学的方法核心",
            "three_layers": {
                "chunk": {
                    "name": "语块",
                    "description": "不是孤立地教单词，而是教搭配使用的词组",
                    "six_categories": [
                        {"category": "定义命名", "purpose": "说明是什么/叫什么", "chunks": "be known as, be called, refer to", "pattern": "It is known as... / It is a kind of..."},
                        {"category": "来源背景", "purpose": "说明何时/何地/为什么", "chunks": "come from, date back to, traditional", "pattern": "It is a traditional... for..."},
                        {"category": "组成材料", "purpose": "说明由什么构成", "chunks": "be made of/from, include, contain", "pattern": "It is made of... / It contains..."},
                        {"category": "过程步骤", "purpose": "说明如何做", "chunks": "first, then, after that, finally", "pattern": "You need to... / Remember to..."},
                        {"category": "特征功能", "purpose": "说明有什么特点/用途", "chunks": "be popular, be easy to, be used to", "pattern": "It is popular because..."},
                        {"category": "评价意义", "purpose": "说明为什么值得介绍", "chunks": "a symbol of, stand for, not only...but also", "pattern": "It has become... / It stands for..."}
                    ]
                },
                "pattern": {
                    "name": "句型",
                    "description": "不是教抽象语法规则，而是教表达特定功能的句式",
                    "principle": "句型教学与语块功能挂钩——先确定表达目的，再教对应句式"
                },
                "task_chain": {
                    "name": "任务链",
                    "description": "不是零散的活动，而是有逻辑递进的任务序列",
                    "three_stages": [
                        {"stage": "学习理解", "focus": "识别、分类、概括", "activities": "感知注意→获取梳理→概括整合"},
                        {"stage": "应用实践", "focus": "分析、比较、推断", "activities": "描述阐释→分析判断→内化应用"},
                        {"stage": "迁移创新", "focus": "评价、论证、创造", "activities": "推理论证→批判评价→创造想象"}
                    ]
                }
            }
        },

        "curriculum_standard_2022": {
            "name": "2022版课标核心要点",
            "description": "基于《义务教育英语课程标准（2022年版）案例式解读》",
            "core_competencies": {
                "name": "核心素养四维",
                "dimensions": [
                    {"name": "语言能力", "mapping": "语言交流目标", "description": "运用语言知识和技能进行理解和表达"},
                    {"name": "文化意识", "mapping": "社会文化目标", "description": "对中外文化的理解和对优秀文化的认同"},
                    {"name": "思维品质", "mapping": "思维认知目标", "description": "思维的逻辑性、批判性、创新性"},
                    {"name": "学习能力", "mapping": "思维认知目标（有效学习策略）", "description": "积极运用和主动调适英语学习策略"}
                ]
            },
            "activity_approach": {
                "name": "英语学习活动观",
                "three_levels": [
                    {"level": "学习理解", "activities": ["感知注意", "获取梳理", "概括整合"]},
                    {"level": "应用实践", "activities": ["描述阐释", "分析判断", "内化应用"]},
                    {"level": "迁移创新", "activities": ["推理论证", "批判评价", "创造想象"]}
                ]
            },
            "key_28_questions": [
                {"id": 1, "section": "课程性质与理念", "question": "英语课程的性质是什么？"},
                {"id": 2, "section": "课程性质与理念", "question": "英语课程的基本理念有哪些？"},
                {"id": 3, "section": "课程性质与理念", "question": "为什么要提出核心素养？"},
                {"id": 4, "section": "课程性质与理念", "question": "英语学习活动观的内涵是什么？"},
                {"id": 5, "section": "课程目标", "question": "核心素养的四个维度是什么？"},
                {"id": 6, "section": "课程目标", "question": "语言能力包含哪些要素？"},
                {"id": 7, "section": "课程目标", "question": "文化意识如何培养？"},
                {"id": 8, "section": "课程目标", "question": "思维品质如何在英语课上发展？"},
                {"id": 9, "section": "课程目标", "question": "学习能力的内涵是什么？"},
                {"id": 10, "section": "课程内容", "question": "课程内容的六个要素是什么？"},
                {"id": 11, "section": "课程内容", "question": "主题如何统领课程内容？"},
                {"id": 12, "section": "课程内容", "question": "语篇在课程内容中的地位？"},
                {"id": 13, "section": "课程内容", "question": "语言知识包含哪些方面？"},
                {"id": 14, "section": "课程内容", "question": "文化知识的教学如何处理？"},
                {"id": 15, "section": "学业质量", "question": "学业质量标准的意义？"},
                {"id": 16, "section": "学业质量", "question": "不同水平如何划分？"},
                {"id": 17, "section": "学业质量", "question": "如何用学业质量标准指导教学？"},
                {"id": 18, "section": "学业质量", "question": "学业质量与评价的关系？"},
                {"id": 19, "section": "课程实施", "question": "如何设计教学目标？"},
                {"id": 20, "section": "课程实施", "question": "如何设计英语学习活动？"},
                {"id": 21, "section": "课程实施", "question": "如何实施教—学—评一体化？"},
                {"id": 22, "section": "课程实施", "question": "如何处理教材内容？"},
                {"id": 23, "section": "课程实施", "question": "如何设计单元整体教学？"},
                {"id": 24, "section": "课程实施", "question": "如何进行读写结合教学？"},
                {"id": 25, "section": "课程实施", "question": "如何实施分层教学？"},
                {"id": 26, "section": "课程实施", "question": "如何设计课堂评价？"},
                {"id": 27, "section": "课程实施", "question": "如何设计作业？"},
                {"id": 28, "section": "课程实施", "question": "如何进行教学反思？"}
            ]
        }
    },

    "teaching_methods": {
        "five_step_closed_loop": {
            "name": "五步闭环法",
            "description": "从文本分析到教学评价的完整闭环",
            "steps": [
                {"step": 1, "name": "文本分析", "description": "明确课文性质定位（引入型/核心型/拓展型），提取核心语块", "output": "预解析表"},
                {"step": 2, "name": "功能分类", "description": "按六类功能对语块进行分类", "output": "功能分类语块表"},
                {"step": 3, "name": "任务链设计", "description": "按学习理解→应用实践→迁移创新设计任务序列", "output": "3课时任务链"},
                {"step": 4, "name": "支架设计", "description": "为不同水平学生提供分层支持", "output": "三层支架方案"},
                {"step": 5, "name": "嵌入式评价", "description": "评价镶嵌在教学过程中", "output": "评价量表和检查点"}
            ]
        },
        "read_write_integration": {
            "name": "读写结合",
            "description": "从阅读输入到写作输出的完整路径",
            "path": "课文阅读→语块提取→口头内化→仿写迁移→独立创作",
            "key_principle": "从读到写之间必须有'口头内化'环节——学生先能说，才能写",
            "common_mistake": "跳过口头环节，直接从读到写，导致'会读不会写'"
        },
        "scaffolding": {
            "name": "分层支架",
            "description": "为不同水平学生提供不同支撑程度",
            "three_levels": [
                {"level": "初阶", "description": "填空仿写——提供句式框架和语块提示", "example": "It is a traditional _____ for _____. It is popular because _____."},
                {"level": "中阶", "description": "改写迁移——提供话题和语块，自己组织句子", "example": "用以下语块写一段关于中国结的介绍：be known as, be made of, stand for"},
                {"level": "高阶", "description": "独立创作——只给话题，自由表达", "example": "向外国朋友介绍一个中国传统节日（100词）"}
            ],
            "key_principle": "三层任务使用同一话题不同支撑程度，不是三个不同题目"
        }
    },

    "teacher_development": {
        "stages": [
            {"stage": "入门期（1-2周）", "focus": "熟悉语块分类，能在课文中圈画", "method": "用三色标注法备课3个单元"},
            {"stage": "实践期（3-6周）", "focus": "设计完整任务链，尝试读写结合课", "method": "选1个单元做完整3课时设计并实施"},
            {"stage": "成熟期（7-12周）", "focus": "熟练运用五步闭环法", "method": "同课异构，与同伴交流改进"},
            {"stage": "引领期（持续）", "focus": "形成个人教学风格，带教新教师", "method": "主持校本教研，分享案例"}
        ]
    },

    "common_misconceptions": {
        "title": "AI辅助教学常见误区",
        "misconceptions": [
            {"wrong": "AI生成=直接用", "right": "AI生成=初稿，必须经过教师三件事干预（明确课文性质、提取核心语块、设计核心问题）"},
            {"wrong": "提示词越详细越好", "right": "提示词需分层：先生成基础框架，再逐级追加要求"},
            {"wrong": "AI能替代教师判断", "right": "AI擅长生成选项，教师擅长做选择——判断力不可外包"},
            {"wrong": "用AI就不需要学方法论", "right": "恰恰相反：不了解方法论，就无法识别AI输出的20%问题"},
            {"wrong": "AI生成的活动都可用", "right": "AI生成的活动常缺乏逻辑串联，需教师检查任务链连贯性"}
        ]
    }
}
