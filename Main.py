import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

# =================================================================
# 1. 配置火山引擎豆包 API (Doubao)
# =================================================================
# 请确保已在火山引擎控制台创建推理接入点
API_KEY = "ark-4a6d7010-d649-4799-ade7-a81ab99a909d-51290"
ENDPOINT_ID = "ep-20260430102926-66md9"

# 初始化豆包 LLM (OpenAI 兼容协议)
doubao_llm = ChatOpenAI(
    openai_api_key=API_KEY,
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    model=ENDPOINT_ID,
    temperature=0.7
)

# =================================================================
# 2. 定义 V-Sync Agent 智能体团队
# =================================================================

# 智能体 1：语义逻辑分析专家
semantic_analyst = Agent(
    role='Semantic Logic Architect (语义逻辑架构师)',
    goal='解析原始剧本的叙事逻辑，并建立全局共享的“视觉锚点”。',
    backstory="""你是一名拥有20年经验的资深影视分镜师。你的专长是从文学剧本中
    提取核心情绪、光源方向、角色位置关系及空间坐标。你的输出将作为整个视觉生成
    流水线的“底层协议”，确保镜头之间逻辑严密。""",
    llm=doubao_llm,
    verbose=True,
    allow_delegation=False
)

# 智能体 2：视觉参数工程专家
parameter_engineer = Agent(
    role='Visual Parameter Engineer (视觉参数工程师)',
    goal='将语义锚点转译为高精度的技术参数提示词（涵盖灯光权重、骨相锚定等）。',
    backstory="""你是一名精通 AI 提示词工程的技术专家。你负责将抽象的视觉描述
    转化为具备工业级确定性的参数，如体素光权重、色彩空间协议、材质反射率等。
    你的任务是确保 AI 模型在不同机位下对主体的理解保持动态对齐。""",
    llm=doubao_llm,
    verbose=True,
    allow_delegation=False
)

# 智能体 3：视觉一致性校验总监
consistency_director = Agent(
    role='Consistency Protocol Director (一致性协议总监)',
    goal='基于 ReAct 机制执行实时交叉熵检测，触发回溯修正以消除视觉漂移。',
    backstory="""你是项目的最后一道质量防线。你通过博弈与校对，检查分镜参数之间
    是否存在特征偏移或环境色温跳变。如果发现不一致，你会要求前置智能体进行
    逻辑修正。你的目标是将视觉一致性废片率降至最低。""",
    llm=doubao_llm,
    verbose=True,
    allow_delegation=True
)

# =================================================================
# 3. 定义任务逻辑 (Tasks)
# =================================================================

def create_vsync_tasks(script_content):
    # 任务 A：剧本建模
    task_analysis = Task(
        description=f"解析以下剧本并提取视觉锚点：\n{script_content}",
        expected_output="一份包含角色坐标、核心光源协议和情绪色调矩阵的视觉逻辑报告。",
        agent=semantic_analyst
    )

    # 任务 B：参数重构
    task_parameterization = Task(
        description="基于视觉逻辑报告，生成一组具备 9 组连续分镜潜力的技术参数指令。",
        expected_output="一组结构化的技术提示词序列，包含物理资产协议和光影控制权重。",
        agent=parameter_engineer
    )

    # 任务 C：协议校验
    task_validation = Task(
        description="审核生成的参数指令，模拟多机位切换，确保不存在逻辑不可逆的视觉漂移。",
        expected_output="一份最终核准的视觉一致性控制协议，或触发修正后的优化方案。",
        agent=consistency_director
    )
    
    return [task_analysis, task_parameterization, task_validation]

# =================================================================
# 4. 执行引擎启动
# =================================================================

if __name__ == "__main__":
    print("🚀 V-Sync Agent 工业级视觉一致性引擎正在启动...")
    
    # 示例输入（你可以修改这里的内容）
    user_script = """
    一个身穿深蓝色制服的宇航员，在充满蒸汽的废弃舱室内行走。
    他手中提着一个散发橙色微光的金属罐。
    特写：宇航员的面罩反射出橙色的火花。
    中景：他走向舱门，环境的光源来自左侧的红色应急灯。
    """

    # 构建任务流
    vsync_crew = Crew(
        agents=[semantic_analyst, parameter_engineer, consistency_director],
        tasks=create_vsync_tasks(user_script),
        process=Process.sequential, # 顺序执行，模拟工业流水线
        verbose=True
    )

    # 开始执行
    result = vsync_crew.kickoff()

    print("\n\n" + "="*50)
    print("✅ V-Sync Agent 任务执行完毕！")
    print("最终输出报告内容：")
    print(result)
    print("="*50)