import os
from crewai import Agent, Task, Crew, Process

# 1. 定义 Agent 角色
class VideoProductionCrew:
    def __init__(self, script_content):
        self.script_content = script_content

    def run(self):
        # 剧本解析 Agent：负责提取情绪曲线和视觉坐标
        script_analyzer = Agent(
            role='Senior Script Analyst',
            goal='Extract emotional arcs and visual coordinates from scripts',
            backstory="""You are an expert at breaking down narratives into visual beats. 
            You focus on 1990s Disney animation aesthetics.""",
            verbose=True,
            allow_delegation=False
        )

        # 参数翻译 Agent：负责将逻辑转化为高密度 Prompt
        prompt_engineer = Agent(
            role='AI Prompt Architect',
            goal='Translate visual beats into high-density technical prompts for Midjourney and Seedence',
            backstory="""You specialize in technical lighting (Amber vs Emerald) and 
            90s hand-drawn textures.""",
            verbose=True
        )

        # 一致性校验 Agent：负责审核镜头间的连贯性
        consistency_checker = Agent(
            role='Visual Continuity Director',
            goal='Ensure character features (glove size, hair) and lighting remain consistent',
            backstory="""You have a sharp eye for detail, ensuring no style drift between panels.""",
            verbose=True
        )

        # 2. 定义任务
        task1 = Task(description=f"Analyze this script: {self.script_content}", agent=script_analyzer)
        task2 = Task(description="Generate 9-panel storyboard prompts based on the analysis.", agent=prompt_engineer)
        task3 = Task(description="Verify visual consistency and format the final output as a JSON report.", agent=consistency_checker)

        # 3. 组建团队
        crew = Crew(
            agents=[script_analyzer, prompt_engineer, consistency_checker],
            tasks=[task1, task2, task3],
            process=Process.sequential # 顺序执行：解析 -> 翻译 -> 校验
        )

        return crew.kickoff()

# 示例调用（以《罐头里的信号》为例）
# script = "A young signalman in an old space station finds an emerald green can..."
# my_project = VideoProductionCrew(script)
# result = my_project.run()