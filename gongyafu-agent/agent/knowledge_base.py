"""
龚亚夫智能体 - 结构化知识库
基于五本著作的完整知识体系
"""

KNOWLEDGE_BASE = {
    "meta": {
        "name": "龚亚夫教学理念知识库",
        "version": "2.0",
        "sources": [
            {
                "id": "tblt",
                "title": "《任务型语言教学》修订版",
                "publisher": "人民教育出版社",
                "year": 2006,
                "pages": 197,
                "description": "任务型语言教学的理论与实践"
            },
            {
                "id": "bfee1",
                "title": "《基础外语教育与研究 第一辑》",
                "publisher": "高等教育出版社",
                "pages": 204,
                "description": "龚亚夫主编的英语教育研究论文集，涵盖多元目标课程、英语教育理念重构、核心素养等"
            },
            {
                "id": "bfee2",
                "title": "《基础外语教育与研究 第二辑》",
                "publisher": "高等教育出版社",
                "pages": 204,
                "description": "续编，涵盖教材评价、教师发展、课堂实践等"
            },
            {
                "id": "case_primary",
                "title": "《案例式解读小学分册》",
                "publisher": "华东师大出版社",
                "year": 2023,
                "pages": 237,
                "description": "基于2022版课标的小学英语教学案例解读"
            },
            {
                "id": "case_junior",
                "title": "《案例式解读初中分册》",
                "publisher": "华东师大出版社",
                "year": 2023,
                "pages": 277,
                "description": "基于2022版课标的初中英语教学案例解读"
            }
        ],
        "constraint": "本知识库仅包含龚亚夫老师五本著作的教学理念，不包含其他来源"
    },

    "core_frameworks": {
        "three_goals": {
            "name": "多元目标英语课程",
            "description": "英语教育应实现三大目标，三者密不可分",
            "theoretical_foundation": {
                "source": "基础外语教育与研究第一辑",
                "core_argument": "英语教育的价值不应仅被定位为工具性学科，它同时具有人文性。语言是思维的载体、文化的窗口、社会交往的媒介。多元目标课程正是基于这一价值重估而提出的课程框架。",
                "key_shifts": [
                    {"from": "英语是工具", "to": "英语既是工具也是素养", "rationale": "语言学习承载着思维培养、文化理解和社会化功能"},
                    {"from": "以语言知识为终点", "to": "以人的发展为终点", "rationale": "语言教育应服务于学生全面发展的需要"},
                    {"from": "教学目标=语言目标", "to": "教学目标=语言+思维+社会文化", "rationale": "语言教学本身就具有多重教育价值"}
                ]
            },
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
                                "阅读关于诚信的故事，讨论'What would you do?'培养判断力",
                                "学习道歉用语时讨论不同情境下的道歉方式，培养换位思考"
                            ],
                            "teaching_implications": "语言材料的选择和任务设计应体现正面价值观引导",
                            "deepening_from_bfee1": "行为规范不是外加的'思想教育'，而是语言使用的内在组成部分——得体的语言使用本身就包含社会规范"
                        },
                        "social_knowledge_integration": {
                            "name": "社会知识与学科融合",
                            "description": "英语不是孤立学科，与历史、地理、科学等学科相连",
                            "examples": [
                                "学习食物词汇时融入营养学知识",
                                "学习天气表达时结合地理知识",
                                "阅读环保话题文章时整合科学和公民教育",
                                "学习动物词汇时结合生物分类知识",
                                "讨论节日时融入历史知识"
                            ],
                            "teaching_implications": "选择跨学科主题的内容，设计需要调用多学科知识的任务"
                        },
                        "multicultural_international": {
                            "name": "多元文化与国际意识",
                            "description": "理解不同文化，形成开放的国际视野",
                            "layers_of_cross_cultural_understanding": {
                                "source": "基础外语教育与研究第一辑",
                                "layer_1": {"name": "表层认知", "description": "了解文化现象（吃什么、穿什么、过什么节）"},
                                "layer_2": {"name": "行为理解", "description": "理解行为背后的价值取向（为什么这样做）"},
                                "layer_3": {"name": "观念反思", "description": "反思自身文化立场，形成文化自觉"},
                                "layer_4": {"name": "融通创造", "description": "在不同文化间建立对话和融合"}
                            },
                            "examples": [
                                "比较中西方节日习俗，理解文化差异",
                                "讨论全球性问题（环保、和平），培养国际意识",
                                "阅读不同国家学生的日常生活，增进理解",
                                "分析同一事件不同媒体的报道角度，理解文化立场"
                            ],
                            "teaching_implications": "不只教'外国文化是什么'，更要引导'为什么不同'和'如何理解'"
                        },
                        "cultural_mission_of_language_education": {
                            "name": "语言教育的文化使命",
                            "description": "语言教育承载着文化传承与交流的使命",
                            "source": "基础外语教育与研究第一辑",
                            "key_points": [
                                "语言是文化最重要的载体，学语言就是进入另一种文化世界",
                                "英语教育的文化使命不只是了解外国文化，也包括用英语表达中国文化",
                                "文化自信不排斥文化理解，真正的文化自信建立在理解基础上",
                                "跨文化交际的核心不是'谁的更好'，而是'理解差异、尊重选择'"
                            ]
                        }
                    }
                },
                "cognitive_thinking": {
                    "name": "思维认知目标",
                    "description": "培养思维能力和学习策略",
                    "thinking_cultivation_path": {
                        "source": "基础外语教育与研究第一辑",
                        "core_argument": "语言与思维不可分割。英语课堂是培养思维能力的天然场所，因为用另一种语言表达思想本身就要求思维的灵活性和精确性。",
                        "specific_paths": [
                            {"path": "从理解到表达", "description": "理解是接受的思维，表达是产出的思维，从理解到表达需要思维层次的提升"},
                            {"path": "从描述到评价", "description": "描述是低阶思维，评价是高阶思维，教学设计应推动学生从描述走向评价"},
                            {"path": "从单一到多元", "description": "单一答案是收敛思维，多元答案是发散思维，英语课堂应鼓励多元思考"},
                            {"path": "从接受到质疑", "description": "接受信息是被动的，质疑信息是批判性的，培养批判性思维从质疑开始"}
                        ]
                    },
                    "sub_dimensions": {
                        "growth_mindset": {
                            "name": "积极心理品质（成长型思维）",
                            "description": "相信自己能通过努力提升，不怕犯错",
                            "examples": [
                                "鼓励学生'I can try'而非'I can't'",
                                "将错误视为学习机会而非失败",
                                "设计有挑战但可达成的任务，让学生体验成功",
                                "用'Yet'思维：'I can't do it YET'暗示进步空间"
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
                            ],
                            "vocabulary_shift": {
                                "source": "基础外语教育与研究第一辑",
                                "title": "从'词表'到'语块'的转变",
                                "core_argument": "传统词汇教学以词表为单位，学生记住孤立的单词和中文释义。但语言使用是以语块为单位的。语块教学不是教学方法的选择问题，而是对语言本质的回归。",
                                "shift_details": [
                                    {"from": "按字母顺序背词表", "to": "按表达功能组织语块"},
                                    {"from": "单词+中文释义", "to": "语块+使用场景+功能"},
                                    {"from": "脱离语境记单词", "to": "在任务中自然习得语块"},
                                    {"from": "关注单词数量", "to": "关注语块质量和使用能力"}
                                ]
                            },
                            "grammar_in_context": {
                                "source": "基础外语教育与研究第一辑",
                                "title": "语法教学的语境化",
                                "core_argument": "语法不是规则，而是资源。语法教学应在语境中呈现，让学生在意义表达中感知语法功能，而非先学规则再套用。",
                                "approach": "感知→归纳→尝试→迁移",
                                "steps": [
                                    {"step": 1, "name": "语境中感知", "description": "在阅读或听力中接触包含目标语法的语篇"},
                                    {"step": 2, "name": "引导归纳", "description": "教师引导学生从例子中归纳语言规律"},
                                    {"step": 3, "name": "控制性尝试", "description": "在半控制的练习中尝试使用新语法"},
                                    {"step": 4, "name": "任务中迁移", "description": "在开放性任务中迁移使用新语法"}
                                ]
                            }
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
                    "teaching_connection": "选择能触动学生内心的材料，设计让学生表达真实感受的活动",
                    "design_implications": [
                        "选择与学生情感体验相关的材料（友谊、家庭、成长）",
                        "设计让学生表达个人态度的讨论活动",
                        "允许学生在任务中融入个人情感和体验"
                    ]
                },
                "knowledge_world": {
                    "name": "知识世界",
                    "description": "学科知识、社会常识、文化理解",
                    "teaching_connection": "语言教学不只是语言知识，还承载着文化知识和社会常识",
                    "design_implications": [
                        "语言材料承载的知识应经过选择，有教育价值",
                        "跨学科内容是语言学习的自然延伸",
                        "文化知识教学应从表层走向深层"
                    ]
                },
                "future_world": {
                    "name": "未来世界",
                    "description": "理想、规划、国际视野、社会责任",
                    "teaching_connection": "设计展望未来的任务，培养国际视野和社会责任感",
                    "design_implications": [
                        "设计需要规划、决策的任务（如设计理想社区）",
                        "引入全球性议题讨论（环保、公平、合作）",
                        "培养学生的社会责任感和国际视野"
                    ]
                }
            }
        },

        "task_based": {
            "name": "任务型语言教学",
            "description": "以'做事情'为驱动的语言教学方式",
            "source": "《任务型语言教学》修订版（人民教育出版社，2006），197页",
            "definition": {
                "core": "任务是'需要人们使用语言来完成的事情'",
                "three_essential_elements": [
                    {"element": "意义优先", "description": "任务关注的是意义表达，而非语言形式的操练。学习者为了表达意义而使用语言，语言形式在意义表达中被自然关注。"},
                    {"element": "有信息差", "description": "任务应包含信息差（information gap），即一方知道另一方不知道的信息，需要通过交流来弥合。没有信息差的活动只是机械操练。"},
                    {"element": "有真实目标", "description": "任务的完成应有真实的交际目标，而不是为了练习而练习。完成任务的结果应是某种有意义的产出。"}
                ]
            },
            "three_phase_model": {
                "name": "前任务—任务环—语言焦点三阶段模式",
                "description": "任务型教学的核心课堂组织模式",
                "phases": {
                    "pre_task": {
                        "name": "前任务（Pre-task）",
                        "purpose": "为任务做准备，激活相关语言和背景知识",
                        "activities": [
                            "引入话题，激活学生已有知识和经验",
                            "呈现完成任务可能需要的新词汇和语块",
                            "听或读与任务相关的示范语篇",
                            "明确任务要求和完成方式"
                        ],
                        "key_principle": "前任务不是教新语言点，而是为完成任务做铺垫",
                        "time_allocation": "约占课时1/5-1/4"
                    },
                    "task_cycle": {
                        "name": "任务环（Task Cycle）",
                        "purpose": "学生在完成任务中使用语言，教师观察并提供支持",
                        "sub_stages": [
                            {"stage": "任务（Task）", "description": "学生结对或小组完成任务，使用现有语言资源解决问题", "focus": "意义表达", "teacher_role": "观察者和支持者，不过度纠正语言错误"},
                            {"stage": "计划（Planning）", "description": "学生准备向全班报告任务结果", "focus": "语言精确性自然提升", "teacher_role": "语言顾问，提供需要的表达支持"},
                            {"stage": "报告（Report）", "description": "学生向全班展示任务结果", "focus": "公开表达", "teacher_role": "组织者和反馈者"}
                        ],
                        "key_principle": "任务环中语言使用从粗放到精确自然过渡",
                        "time_allocation": "约占课时1/2-3/5"
                    },
                    "language_focus": {
                        "name": "语言焦点（Language Focus）",
                        "purpose": "在完成任务后聚焦语言形式",
                        "activities": [
                            "分析任务中使用的语言特征",
                            "练习和巩固关键语言表达",
                            "将新语言与已有知识建立联系"
                        ],
                        "key_principle": "语言焦点在任务之后而非之前——先有使用需求，再聚焦形式",
                        "time_allocation": "约占课时1/5-1/4"
                    }
                }
            },
            "task_types": {
                "name": "任务的六种类型",
                "description": "根据认知操作对任务进行分类",
                "types": [
                    {
                        "type": "列举型（Listing）",
                        "description": "列举事物、特征、理由等",
                        "cognitive_level": "低阶-中阶",
                        "example": "列举健康饮食应包含的食物种类",
                        "thinking_focus": "回忆、分类"
                    },
                    {
                        "type": "排序型（Ordering/Sorting）",
                        "description": "按标准对信息进行排序或分类",
                        "cognitive_level": "中阶",
                        "example": "将日常活动按时间顺序排列，或按健康程度排序",
                        "thinking_focus": "比较、分类"
                    },
                    {
                        "type": "比较型（Comparing）",
                        "description": "比较异同，发现差异",
                        "cognitive_level": "中阶-高阶",
                        "example": "比较中西方节日庆祝方式的异同",
                        "thinking_focus": "分析、比较"
                    },
                    {
                        "type": "问题解决型（Problem Solving）",
                        "description": "面对问题，寻找解决方案",
                        "cognitive_level": "高阶",
                        "example": "帮奶奶找公交卡——给定情境，需要推理和决策",
                        "thinking_focus": "分析、推断、评价"
                    },
                    {
                        "type": "分享个人经验型（Sharing Personal Experience）",
                        "description": "基于个人经历进行交流",
                        "cognitive_level": "中阶-高阶",
                        "example": "分享一次难忘的旅行经历，并讨论收获",
                        "thinking_focus": "描述、反思、评价"
                    },
                    {
                        "type": "创造性任务（Creative Tasks）",
                        "description": "设计、创造新的内容",
                        "cognitive_level": "高阶",
                        "example": "设计一个理想的学校午餐菜单，考虑营养、口味和文化",
                        "thinking_focus": "创造、评价"
                    }
                ]
            },
            "task_difficulty_factors": {
                "name": "任务难度四因素",
                "description": "选择和设计任务时需要考虑的难度因素",
                "factors": [
                    {
                        "factor": "语言复杂度",
                        "description": "任务所需语言的复杂程度",
                        "adjustment": "简化语言输入，提供语块支架，降低语言要求"
                    },
                    {
                        "factor": "认知负荷",
                        "description": "任务对思维操作的要求",
                        "adjustment": "从简单列举到复杂推理，渐进提升认知要求"
                    },
                    {
                        "factor": "交际压力",
                        "description": "任务对即时产出的压力",
                        "adjustment": "从准备充分的报告到即时对话，渐进增加压力"
                    },
                    {
                        "factor": "话题熟悉度",
                        "description": "学生对任务话题的熟悉程度",
                        "adjustment": "先选择熟悉话题，再扩展到不熟悉话题"
                    }
                ],
                "application": "设计任务链时，应从低难度因素组合向高难度因素组合过渡"
            },
            "traditional_vs_task_comparison": {
                "name": "传统教学vs任务型教学对比",
                "dimensions": [
                    {"dimension": "出发点", "traditional": "从语言形式出发", "task_based": "从意义和任务出发"},
                    {"dimension": "教学目标", "traditional": "掌握语言知识", "task_based": "完成任务，在任务中学习语言"},
                    {"dimension": "活动性质", "traditional": "操练（drill）为主", "task_based": "真实交际（communication）为主"},
                    {"dimension": "学生角色", "traditional": "被动接受和重复", "task_based": "主动参与和创造"},
                    {"dimension": "错误处理", "traditional": "即时纠正", "task_based": "意义优先，不中断交际"},
                    {"dimension": "评价标准", "traditional": "语言准确性", "task_based": "任务完成度和语言得体性"}
                ]
            },
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
                    "goal_dimension": "社会文化目标+语言交流目标",
                    "task_type": "比较型+分享个人经验型",
                    "three_phase": {
                        "pre_task": "讨论：你打喷嚏时怎么办？不同国家的人怎么反应？",
                        "task_cycle": "小组调查不同文化的礼貌表达，制作'礼貌用语手册'",
                        "language_focus": "总结礼貌表达的结构和语块"
                    }
                },
                {
                    "name": "判断好朋友",
                    "description": "用英语讨论友情标准，训练评价和论证思维",
                    "goal_dimension": "思维认知目标+语言交流目标",
                    "task_type": "比较型+问题解决型",
                    "three_phase": {
                        "pre_task": "阅读关于友情的短文，提取关键品质词",
                        "task_cycle": "小组讨论：好朋友最重要的三个品质是什么？排序并论证",
                        "language_focus": "表达观点和论证的语块：I think... because... / In my opinion... / The most important thing is..."
                    }
                },
                {
                    "name": "帮奶奶找公交卡",
                    "description": "模拟真实问题解决场景",
                    "goal_dimension": "语言交流目标+思维认知目标",
                    "task_type": "问题解决型",
                    "three_phase": {
                        "pre_task": "呈现情境：奶奶找不到公交卡，可能在哪里？",
                        "task_cycle": "小组推理：根据线索判断卡片可能的位置，制定寻找方案",
                        "language_focus": "表达推测和判断的语块：It might be... / She probably... / I guess..."
                    }
                },
                {
                    "name": "Jimmy日常作息",
                    "description": "从个人信息出发，拓展到生活习惯比较",
                    "goal_dimension": "三目标融合",
                    "task_type": "比较型+分享个人经验型",
                    "three_phase": {
                        "pre_task": "阅读Jimmy的日常作息表，提取时间表达和活动语块",
                        "task_cycle": "比较自己的作息与Jimmy的，讨论健康习惯",
                        "language_focus": "时间表达和频率副词语块"
                    }
                }
            ]
        },

        "chunk_pattern_task": {
            "name": "语块—句型—任务链",
            "description": "龚亚夫任务型教学的方法核心",
            "detailed_operation": {
                "source": "任务型语言教学+基础外语教育与研究第一辑",
                "step_by_step": [
                    {"step": 1, "name": "确定表达功能", "description": "分析本课内容，确定学生需要表达什么功能（定义、描述、比较、评价等）"},
                    {"step": 2, "name": "提取功能语块", "description": "根据表达功能从课文中提取对应语块，按六类功能分类"},
                    {"step": 3, "name": "匹配功能句型", "description": "将语块与句型挂钩——表达什么功能用什么句式"},
                    {"step": 4, "name": "设计任务链", "description": "按学习理解→应用实践→迁移创新设计递进任务"},
                    {"step": 5, "name": "设计支架", "description": "为不同水平学生提供不同支撑程度的支架"},
                    {"step": 6, "name": "嵌入评价", "description": "评价镶嵌在教学过程中，而非课后附加"}
                ]
            },
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
            "description": "基于《义务教育英语课程标准（2022年版）案例式解读》小学分册和初中分册",
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
        },

        "basic_foreign_ed_vol1": {
            "name": "基础外语教育与研究 第一辑",
            "description": "龚亚夫主编的英语教育研究论文集，涵盖多元目标课程、英语教育理念重构、核心素养等",
            "source": "《基础外语教育与研究 第一辑》（高等教育出版社），204页",
            "core_themes": {
                "value_reassessment": {
                    "name": "英语教育的价值重估",
                    "core_argument": "英语教育的价值不应仅被定位为工具性。语言是思维的载体、文化的窗口、社会交往的媒介。将英语教育仅视为'工具学科'是对其价值的低估。",
                    "dual_nature": {
                        "instrumental": "工具性——语言作为交际工具",
                        "humanistic": "人文性——语言作为思维培养、文化理解和社会化的媒介",
                        "integration": "工具性和人文性不是对立的，而是统一的。在完成任务的过程中，工具性和人文性同时实现。"
                    }
                },
                "theoretical_foundation_of_multi_goal": {
                    "name": "多元目标课程的理论基础",
                    "foundations": [
                        {"foundation": "社会文化理论", "description": "语言学习不是孤立的认知过程，而是发生在社会文化情境中的意义建构过程"},
                        {"foundation": "全人教育理念", "description": "教育的终极目标是人的全面发展，语言教育应服务于这一目标"},
                        {"foundation": "核心素养框架", "description": "核心素养为多元目标课程提供了新的表述框架，但核心理念是一致的"},
                        {"foundation": "任务型教学理论", "description": "任务型教学为多元目标的实现提供了方法论支撑"}
                    ]
                },
                "core_competencies_landing": {
                    "name": "核心素养在英语教学中的落地",
                    "key_points": [
                        "核心素养不是外加的标签，而是教学设计的内在逻辑",
                        "语言能力是基础，但在语言学习中同时发展思维品质、文化意识、学习能力",
                        "每一节课都应思考：这节课发展了学生哪个素养维度？",
                        "素养导向的教学设计从目标开始就是整合的，而非分项的"
                    ]
                },
                "thinking_cultivation": {
                    "name": "语言教育中的思维培养",
                    "key_points": [
                        "语言与思维不可分割——用另一种语言思考本身就是思维训练",
                        "不同课型有不同的思维培养重点：阅读课侧重分析和推断，写作课侧重组织和创造",
                        "提问是思维培养的钥匙——教师的提问层次决定学生的思维层次",
                        "从封闭性问题到开放性问题的转变是思维培养的关键"
                    ]
                },
                "vocabulary_to_chunk": {
                    "name": "词汇教学从'词表'到'语块'的转变",
                    "core_argument": "传统词汇教学以词表为单位，但语言使用以语块为单位。语块教学不是方法选择，而是对语言本质的回归。",
                    "shift_details": [
                        {"from": "按字母顺序背词表", "to": "按表达功能组织语块"},
                        {"from": "单词+中文释义", "to": "语块+使用场景+功能"},
                        {"from": "脱离语境记单词", "to": "在任务中自然习得语块"},
                        {"from": "关注单词数量", "to": "关注语块质量和使用能力"}
                    ]
                },
                "grammar_contextualization": {
                    "name": "语法教学的语境化",
                    "core_argument": "语法不是规则，而是资源。语法教学应在语境中呈现，让学生在意义表达中感知语法功能。",
                    "approach": "感知→归纳→尝试→迁移"
                }
            }
        },

        "basic_foreign_ed_vol2": {
            "name": "基础外语教育与研究 第二辑",
            "description": "续编，涵盖教材评价、教师发展、课堂实践等",
            "source": "《基础外语教育与研究 第二辑》（高等教育出版社），204页",
            "core_themes": {
                "textbook_evaluation": {
                    "name": "教材评价体系",
                    "dual_dimension_framework": {
                        "name": "教材评价双维度框架",
                        "dimension_1": {
                            "name": "本体结构性（6项）",
                            "items": [
                                {"item": "目标一致性", "description": "教材目标与课程标准的一致程度"},
                                {"item": "内容科学性", "description": "教材内容的准确性和科学性"},
                                {"item": "结构系统性", "description": "教材编排的系统性逻辑性"},
                                {"item": "语言真实性", "description": "教材语言的真实性和地道性"},
                                {"item": "活动有效性", "description": "教材活动设计的有效性"},
                                {"item": "配套完整性", "description": "教材配套资源的完整性"}
                            ]
                        },
                        "dimension_2": {
                            "name": "主体适切性（6项）",
                            "items": [
                                {"item": "学生适切性", "description": "教材内容与学生认知水平的匹配度"},
                                {"item": "教师适切性", "description": "教材对教师专业发展的支持度"},
                                {"item": "情境适切性", "description": "教材内容与本地教学情境的适配度"},
                                {"item": "文化适切性", "description": "教材文化内容与学生文化背景的关联度"},
                                {"item": "发展适切性", "description": "教材对学生不同发展需求的支持度"},
                                {"item": "使用适切性", "description": "教材使用的便利性和灵活性"}
                            ]
                        }
                    },
                    "textbook_secondary_development": {
                        "name": "教材内容的二次开发",
                        "description": "教师应根据实际教学需要对教材进行创造性使用",
                        "principles": [
                            "教材是教学的资源而非圣经",
                            "二次开发不是否定教材，而是让教材更好地服务学生",
                            "开发的三种方式：调整顺序、补充内容、改编活动",
                            "开发的依据：学生实际水平、本地教学情境、核心素养目标"
                        ]
                    }
                },
                "teacher_professional_development": {
                    "name": "教师专业发展",
                    "stage_model": {
                        "name": "教师专业发展阶段模型",
                        "stages": [
                            {"stage": "生存期", "years": "1-3年", "focus": "站稳课堂，熟悉教材，完成基本教学任务", "support_needed": "导师指导、集体备课、课堂观摩"},
                            {"stage": "适应期", "years": "3-5年", "focus": "灵活处理教材，形成基本教学策略", "support_needed": "同伴互助、教学研讨、专题培训"},
                            {"stage": "发展期", "years": "5-10年", "focus": "形成教学风格，能进行教学反思和研究", "support_needed": "课题研究、学术交流、带教指导"},
                            {"stage": "成熟期", "years": "10年以上", "focus": "教学创新引领，形成教育思想", "support_needed": "平台搭建、成果推广、学术写作"}
                        ]
                    },
                    "reflection_levels": {
                        "name": "教学反思的层次与策略",
                        "levels": [
                            {"level": "技术性反思", "description": "反思教学技术和方法：这节课的活动有效吗？时间分配合理吗？"},
                            {"level": "实践性反思", "description": "反思教学决策和判断：为什么选这个活动？这个判断对吗？"},
                            {"level": "批判性反思", "description": "反思教学信念和假设：我的教学理念是什么？这个理念从何而来？它还适用吗？"}
                        ]
                    },
                    "collaborative_learning": {
                        "name": "教师合作学习",
                        "forms": [
                            {"form": "集体备课", "description": "共同分析教材、设计教学、分享资源"},
                            {"form": "课堂观察", "description": "有目的地观察同伴课堂，提供反馈"},
                            {"form": "同课异构", "description": "同一课题不同设计，比较反思"},
                            {"form": "行动研究", "description": "在教学中发现问题，通过系统研究改进实践"}
                        ]
                    }
                },
                "classroom_observation": {
                    "name": "课堂观察的维度与方法",
                    "dimensions": [
                        {"dimension": "教师维度", "focus": "教学目标的设定与达成、教学活动的组织与引导、提问的层次与反馈"},
                        {"dimension": "学生维度", "focus": "参与度、思维活跃度、语言产出质量"},
                        {"dimension": "内容维度", "focus": "语言输入的质量、任务设计的有效性、语块呈现的系统性"},
                        {"dimension": "过程维度", "focus": "任务链的逻辑性、活动过渡的流畅性、评价嵌入的及时性"}
                    ],
                    "methods": [
                        {"method": "定量观察", "description": "记录提问类型、等待时间、学生参与人次等"},
                        {"method": "定性观察", "description": "描述关键事件、记录课堂生态"},
                        {"method": "聚焦观察", "description": "选择一两个维度深入观察"}
                    ]
                },
                "school_based_research": {
                    "name": "校本教研的组织与实施",
                    "key_points": [
                        "校本教研应以问题为导向，从教学实践中发现问题",
                        "教研活动应形成'实践-反思-改进'的循环",
                        "校本教研不是形式主义，应聚焦真实的教学问题",
                        "校长和教研组长的专业引领是校本教研质量的关键"
                    ]
                },
                "action_research": {
                    "name": "课题研究的基本方法",
                    "steps": [
                        {"step": 1, "name": "发现问题", "description": "从教学实践中识别值得研究的问题"},
                        {"step": 2, "name": "设计方案", "description": "制定研究计划和实施方案"},
                        {"step": 3, "name": "实施行动", "description": "在教学中实施改进方案"},
                        {"step": 4, "name": "观察反思", "description": "收集数据，分析效果，反思调整"},
                        {"step": 5, "name": "循环改进", "description": "基于反思调整方案，进入下一轮循环"}
                    ]
                }
            }
        },

        "primary_cases": {
            "name": "小学英语教学案例",
            "description": "基于《案例式解读小学分册》的典型教学案例",
            "source": "《案例式解读小学分册》（华东师大出版社，2023），237页",
            "course_nature_and_concept": {
                "name": "小学英语课程性质与理念",
                "key_points": [
                    "小学英语课程具有基础性、实践性和综合性的特征",
                    "小学阶段重在激发兴趣、培养语感、建立信心",
                    "语言学习与儿童认知发展水平相适应",
                    "从做中学、从玩中学是小学英语的基本路径"
                ]
            },
            "core_competencies_age_features": {
                "name": "小学英语核心素养的年龄特点",
                "language_ability": "以听说为主，读写逐步引入；语音意识优先于拼写能力",
                "cultural_awareness": "从感知文化现象开始，不宜过早进行深层文化分析",
                "thinking_quality": "以具体形象思维为主，逐步发展抽象思维；提问应以具象问题为主",
                "learning_ability": "培养良好的学习习惯比掌握知识更重要"
            },
            "activity_approach_adaptation": {
                "name": "小学英语学习活动观的适配",
                "adaptation_principles": [
                    "学习理解层：多用TPR、图片、歌曲、故事等直观方式",
                    "应用实践层：多设计角色扮演、信息差游戏、简单调查等互动活动",
                    "迁移创新层：从简单创作（画+说）逐步过渡到综合创作（写+说）",
                    "活动时间短、节奏快，符合小学生注意力特点"
                ]
            },
            "phonics_teaching": {
                "name": "小学英语语音教学",
                "key_points": [
                    "语音教学应渗透在日常教学中，而非集中教授规则",
                    "从语感培养入手：多听多读多模仿，先感受后归纳",
                    "自然拼读（Phonics）是小学语音教学的重要方法",
                    "语音教学应与词汇教学结合，在语块中感知发音规律"
                ]
            },
            "vocabulary_teaching_primary": {
                "name": "小学英语词汇教学（语块起步）",
                "key_points": [
                    "小学阶段从语块起步，不是先学单词再组合",
                    "常用语块先整体输入，再逐步分析内部结构",
                    "在歌曲、韵文、故事中自然习得语块",
                    "词汇评价不以单词量为唯一标准，应关注语块的使用能力"
                ]
            },
            "classroom_management": {
                "name": "小学英语课堂管理",
                "key_points": [
                    "课堂用语应简洁、重复、配动作，帮助学生理解",
                    "活动规则要明确、示范要充分、过渡要流畅",
                    "小组活动要有角色分工，避免'一人做、其他人看'",
                    "评价以鼓励为主，用具体表扬替代笼统称赞"
                ]
            },
            "primary_assessment": {
                "name": "小学英语评价方式",
                "formative_assessment": {
                    "name": "形成性评价",
                    "methods": ["课堂观察记录", "学习档案袋", "学生自评表", "同伴互评"],
                    "key_principle": "关注进步而非排名，关注过程而非结果"
                },
                "performance_assessment": {
                    "name": "表现性评价",
                    "methods": ["角色扮演", "项目作品", "口头报告", "绘本创作"],
                    "key_principle": "让学生在真实任务中展示能力，而非纸笔测试"
                }
            },
            "typical_cases": [
                {
                    "name": "小学英语食物主题单元设计",
                    "grade": "四年级",
                    "goal_integration": "语言交流（食物语块）+社会文化（健康饮食观念）+思维认知（分类比较）",
                    "task_chain": [
                        "学习理解：看食物图片，学习语块（a piece of bread, a glass of milk等）",
                        "应用实践：设计健康午餐菜单，比较不同搭配",
                        "迁移创新：制作班级'健康饮食手册'，用英语介绍推荐搭配"
                    ]
                },
                {
                    "name": "小学英语动物主题单元设计",
                    "grade": "三年级",
                    "goal_integration": "语言交流（动物描述语块）+社会文化（动物保护意识）+思维认知（分类比较）",
                    "task_chain": [
                        "学习理解：听动物描述猜动物，学习描述语块",
                        "应用实践：小组制作动物信息卡，比较不同动物",
                        "迁移创新：设计'我心中的动物园'并做英文介绍"
                    ]
                }
            ]
        },

        "junior_cases": {
            "name": "初中英语教学案例",
            "description": "基于《案例式解读初中分册》的典型教学案例",
            "source": "《案例式解读初中分册》（华东师大出版社，2023），277页",
            "course_objective_design": {
                "name": "初中英语课程目标设计",
                "key_points": [
                    "教学目标应基于核心素养四维，而非单纯的知识与技能",
                    "目标表述应可观察、可评价，避免'培养学生的…'等笼统表述",
                    "单元目标→课时目标应有清晰的层级关系",
                    "每课时目标应体现不同素养维度的整合"
                ]
            },
            "unit_whole_teaching": {
                "name": "初中英语单元整体教学",
                "key_points": [
                    "单元是教学的基本单位，课时设计应服务于单元整体目标",
                    "单元整体教学的步骤：解读单元主题→确定单元目标→划分课时→设计任务链→嵌入评价",
                    "语篇分析是单元整体教学的基础：每篇语篇的功能定位不同",
                    "单元内课时之间应有逻辑递进，而非并列堆砌"
                ]
            },
            "read_write_integration_junior": {
                "name": "初中英语读写结合教学",
                "key_points": [
                    "读写结合是初中英语教学的核心路径",
                    "读为输入：从阅读中提取可迁移的语块和结构",
                    "写为输出：基于输入进行有支撑的写作",
                    "中间环节：口头内化——从读到写之间必须有说",
                    "写作评价应有明确量表，包含内容、结构、语言三个维度"
                ]
            },
            "grammar_teaching_junior": {
                "name": "初中英语语法教学（语境中呈现）",
                "key_points": [
                    "语法教学不是先规则后练习，而是先语境后归纳",
                    "在阅读中感知语法→引导归纳规律→控制性尝试→任务中迁移",
                    "语法教学应关注语法的表意功能，而非仅关注形式",
                    "同一语法现象在不同语篇中反复出现，加深理解"
                ]
            },
            "listening_speaking_junior": {
                "name": "初中英语听说教学",
                "key_points": [
                    "听前：激活背景知识，预教关键词块，明确听力目的",
                    "听中：从主旨到细节，设计不同层次的听力任务",
                    "听后：从听力理解到口头产出，设计有信息差的说的活动",
                    "听说结合：听为输入，说为输出，中间有理解到表达的转换"
                ]
            },
            "differentiated_teaching_junior": {
                "name": "初中英语分层教学",
                "key_points": [
                    "分层不是分班，而是同一班级内提供不同支撑",
                    "三层支架：初阶填空仿写→中阶改写迁移→高阶独立创作",
                    "分层的关键：同一话题不同支撑程度，不是不同题目",
                    "评价分层：不同层次有不同的达标标准"
                ]
            },
            "teaching_learning_assessment_integration": {
                "name": "教-学-评一体化",
                "key_points": [
                    "教学、学习、评价是一个整体，不是三个分离的环节",
                    "教学目标就是学习目标，也是评价标准",
                    "评价镶嵌在教学过程中，而非课后附加",
                    "评价的主要功能是促进学习（assessment for learning），而非仅仅评定等级",
                    "每个教学环节都应有对应的评价检查点"
                ]
            },
            "homework_design_junior": {
                "name": "初中英语作业设计",
                "key_points": [
                    "作业应与课堂学习目标一致，而非脱离的额外负担",
                    "作业类型应多样化：理解型、应用型、创造型",
                    "分层作业：基础必做+拓展选做",
                    "作业反馈应及时、具体，指向改进而非仅打分"
                ]
            },
            "junior_assessment": {
                "name": "初中英语教学评价",
                "key_points": [
                    "过程性评价与终结性评价结合",
                    "评价维度应多元：语言、思维、文化、策略",
                    "学生参与评价：自评、互评培养元认知",
                    "评价结果应用于改进教学，而非仅仅归档"
                ]
            },
            "typical_cases": [
                {
                    "name": "初中英语'节日文化'单元整体教学",
                    "grade": "八年级",
                    "unit_goal": "用英语介绍中国传统节日，理解文化差异，表达文化自信",
                    "task_chain": [
                        "课时1（学习理解）：阅读中西方节日语篇，提取描述节日的语块和句型",
                        "课时2（应用实践）：比较中西方节日异同，制作节日信息卡",
                        "课时3（迁移创新）：向外国朋友介绍一个中国传统节日（口头+书面）"
                    ],
                    "assessment_integration": "课时1检查语块提取→课时2检查比较分析→课时3评估综合产出"
                },
                {
                    "name": "初中英语'环境保护'读写结合教学",
                    "grade": "九年级",
                    "unit_goal": "阅读环保文章，提取论证语块，写一篇环保倡议书",
                    "task_chain": [
                        "课时1（学习理解）：阅读环保文章，提取论证语块（We should... / It is important to... / If we don't...）",
                        "课时2（应用实践）：讨论校园环保问题，用所学语块口头表达建议",
                        "课时3（迁移创新）：写一篇'绿色校园倡议书'，要求使用至少5个论证语块"
                    ],
                    "assessment_integration": "课时1检查语块识别→课时2检查口头表达→课时3用写作量表评估"
                }
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
        "three_phase_implementation": {
            "name": "三阶段课堂实施",
            "description": "基于任务型教学的前任务-任务环-语言焦点模式",
            "source": "《任务型语言教学》",
            "phases": [
                {
                    "phase": "前任务",
                    "time": "约10分钟",
                    "activities": ["引入话题", "激活背景知识", "呈现关键词块", "听/读示范语篇"],
                    "teacher_role": "引导者和资源提供者"
                },
                {
                    "phase": "任务环",
                    "time": "约25分钟",
                    "activities": ["小组完成任务", "准备报告", "全班展示"],
                    "teacher_role": "观察者、支持者和组织者"
                },
                {
                    "phase": "语言焦点",
                    "time": "约10分钟",
                    "activities": ["分析语言特征", "练习关键表达", "建立新旧联系"],
                    "teacher_role": "语言分析引导者"
                }
            ]
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
        },
        "question_design": {
            "name": "提问设计",
            "description": "教师提问层次决定学生思维层次",
            "source": "基础外语教育与研究第一辑",
            "three_levels": [
                {"level": "展示性问题", "purpose": "检查理解", "examples": ["What did the boy do?", "Where is the park?"], "thinking_demand": "低"},
                {"level": "参阅性问题", "purpose": "引导分析", "examples": ["Why do you think he did that?", "How are these two stories different?"], "thinking_demand": "中"},
                {"level": "评价性问题", "purpose": "促进批判性思维", "examples": ["Do you agree with this approach? Why?", "What would you do differently?"], "thinking_demand": "高"}
            ],
            "key_principle": "每节课都应有三种层次的问题，且高阶问题比例应逐步增加"
        }
    },

    "teacher_development": {
        "stages": [
            {"stage": "入门期（1-2周）", "focus": "熟悉语块分类，能在课文中圈画", "method": "用三色标注法备课3个单元"},
            {"stage": "实践期（3-6周）", "focus": "设计完整任务链，尝试读写结合课", "method": "选1个单元做完整3课时设计并实施"},
            {"stage": "成熟期（7-12周）", "focus": "熟练运用五步闭环法", "method": "同课异构，与同伴交流改进"},
            {"stage": "引领期（持续）", "focus": "形成个人教学风格，带教新教师", "method": "主持校本教研，分享案例"}
        ],
        "professional_stages_from_bfee2": {
            "name": "教师专业发展阶段模型",
            "source": "基础外语教育与研究第二辑",
            "stages": [
                {"stage": "生存期", "years": "1-3年", "focus": "站稳课堂，熟悉教材，完成基本教学任务", "support_needed": "导师指导、集体备课、课堂观摩"},
                {"stage": "适应期", "years": "3-5年", "focus": "灵活处理教材，形成基本教学策略", "support_needed": "同伴互助、教学研讨、专题培训"},
                {"stage": "发展期", "years": "5-10年", "focus": "形成教学风格，能进行教学反思和研究", "support_needed": "课题研究、学术交流、带教指导"},
                {"stage": "成熟期", "years": "10年以上", "focus": "教学创新引领，形成教育思想", "support_needed": "平台搭建、成果推广、学术写作"}
            ]
        },
        "reflection_framework": {
            "name": "教学反思框架",
            "source": "基础外语教育与研究第二辑",
            "three_levels": [
                {"level": "技术性反思", "description": "反思教学技术和方法：这节课的活动有效吗？时间分配合理吗？", "guiding_questions": ["学生参与度如何？", "活动时间分配合理吗？", "教学目标达成了吗？"]},
                {"level": "实践性反思", "description": "反思教学决策和判断：为什么选这个活动？这个判断对吗？", "guiding_questions": ["为什么选择这个任务？", "有没有更好的替代方案？", "学生实际需求与设计假设一致吗？"]},
                {"level": "批判性反思", "description": "反思教学信念和假设：我的教学理念是什么？它还适用吗？", "guiding_questions": ["我为什么要这样教？", "这种教法的理论依据是什么？", "有没有我未意识到的偏见或假设？"]}
            ]
        },
        "collaborative_learning": {
            "name": "教师合作学习",
            "source": "基础外语教育与研究第二辑",
            "forms": [
                {"form": "集体备课", "description": "共同分析教材、设计教学、分享资源"},
                {"form": "课堂观察", "description": "有目的地观察同伴课堂，提供反馈"},
                {"form": "同课异构", "description": "同一课题不同设计，比较反思"},
                {"form": "行动研究", "description": "在教学中发现问题，通过系统研究改进实践"}
            ]
        }
    },

    "common_misconceptions": {
        "title": "AI辅助教学常见误区",
        "misconceptions": [
            {"wrong": "AI生成=直接用", "right": "AI生成=初稿，必须经过教师三件事干预（明确课文性质、提取核心语块、设计核心问题）"},
            {"wrong": "提示词越详细越好", "right": "提示词需分层：先生成基础框架，再逐级追加要求"},
            {"wrong": "AI能替代教师判断", "right": "AI擅长生成选项，教师擅长做选择——判断力不可外包"},
            {"wrong": "用AI就不需要学方法论", "right": "恰恰相反：不了解方法论，就无法识别AI输出的20%问题"},
            {"wrong": "AI生成的活动都可用", "right": "AI生成的活动常缺乏逻辑串联，需教师检查任务链连贯性"},
            {"wrong": "任务型教学=不做语言练习", "right": "任务型教学不是取消语言练习，而是将语言练习嵌入任务，先有意义需求再聚焦形式"},
            {"wrong": "多元目标=什么都教", "right": "多元目标不是面面俱到，而是有主有次、有机整合，每节课有1-2个重点目标"},
            {"wrong": "语块教学=背词组", "right": "语块教学不是简单背词组，而是在任务中理解语块的功能和使用场景"},
            {"wrong": "分层教学=分班教学", "right": "分层教学是在同一班级内提供不同支撑程度，不是按水平分班"},
            {"wrong": "教-学-评一体化=每节课都考试", "right": "教-学-评一体化是评价镶嵌在教学过程中，通过观察、提问、检查等方式促进学习，不是频繁考试"},
            {"wrong": "语境化语法=不讲语法规则", "right": "语境化语法不是不讲规则，而是先在语境中感知、再引导归纳规则，比直接告诉规则更深刻"},
            {"wrong": "核心素养是课标的新要求，以前没有", "right": "核心素养是多元目标课程的现代表述，核心理念一致。龚亚夫的多元目标课程（社会文化+思维认知+语言交流）与核心素养四维（文化意识+思维品质+学习能力+语言能力）是对应的"}
        ]
    }
}
