import os
from crewai import Agent, Task, Crew, Process

# 核心系统：V-Sync (Visual Sync) 影视一致性控制引擎
class VSyncProductionEngine:
    def __init__(self, prompt_content):
        self.prompt_content = prompt_content

    def run(self):
        # 1. 语义深度解析 Agent (Semantic Analyst)
        # 负责解构叙事逻辑，建立跨镜头的时空锚点
        semantic_analyst = Agent(
            role='Semantic Logic Architect',
            goal='Deconstruct narrative logic and establish global visual anchors from raw input',
            backstory="""You are a master of cinematographic reasoning. Your job is to 
            transform abstract descriptions into a structured visual foundation, 
            ensuring that time, space, and emotional tone are logically mapped 
            across the entire sequence.""",
            verbose=True,
            allow_delegation=False
        )

        # 2. 智能参数优化 Agent (Parameter Architect)
        # 负责将语义锚点转译为高密度、高确定性的技术参数指令
        parameter_engineer = Agent(
            role='Visual Parameter Engineer',
            goal='Translate semantic anchors into high-density technical prompts with precise parameter locking',
            backstory="""You specialize in technical lighting, character structural integrity, 
            and asset consistency protocols. You ensure that bone structure, material 
            texture, and volumetric lighting weights are mathematically aligned across all shots.""",
            verbose=True
        )

        # 3. 视觉一致性校验 Agent (Continuity Validator)
        # 基于 ReAct 机制执行闭环修复，确保输出符合影视级连续性标准
        continuity_validator = Agent(
            role='Consistency Protocol Director',
            role_description='Execute ReAct loops to ensure cross-shot visual logic matching',
            goal='Perform cross-entropy checks on multi-panel sequences to eliminate visual drift',
            backstory="""You have a zero-tolerance policy for logic contradictions. 
            You detect and fix drifts in facial structure, color temperature, and asset 
            placement by triggering backtracking and prompt re-optimization.""",
            verbose=True
        )

        # 2. 定义长链推理任务 (Long-chain Reasoning Tasks)
        # 任务一：语义建模
        task1 = Task(
            description=f"Analyze the following input and establish a global visual anchor system: {self.prompt_content}", 
            agent=semantic_analyst
        )
        
        # 任务二：参数编排与高密度 Prompt 生成
        task2 = Task(
            description="Generate high-density technical prompts for a 9-panel sequence, ensuring parameter alignment for all key assets.", 
            agent=parameter_engineer
        )
        
        # 任务三：视觉协议校验与闭环优化
        task3 = Task(
            description="Execute a cross-shot consistency audit. Verify visual protocol adherence and format the final consistent prompt set as a JSON report.", 
            agent=continuity_validator
        )

        # 3. 组建多 Agent 协作团队
        v_sync_crew = Crew(
            agents=[semantic_analyst, parameter_engineer, continuity_validator],
            tasks=[task1, task2, task3],
            process=Process.sequential # 顺序执行：语义解析 -> 参数编排 -> 一致性校验
        )

        return v_sync_crew.kickoff()

# 示例调用
# user_input = "在此处输入您的创意剧本或分镜描述..."
# engine = VSyncProductionEngine(user_input)
# final_protocol = engine.run()