# V-Sync Agent  (Visual Sync Agent)

这是一个基于 **CrewAI** 多智能体协作框架构建的自动化影视工业化管线，旨在解决 AIGC 视频创作中“视觉协议失控”与“跨镜头一致性缺失”的核心痛点。

## 核心功能模块

### 1. 语义深度解析层 (Semantic Analyst Agent)
* **功能逻辑**：通过 LLM 深度解构原始 Prompt 或剧本。它不只是提取文字，而是识别镜头间的时间轴关系、空间位移和情绪基调。
* **输出**：建立全局“视觉底座”，为后续分镜生成提供确定性的逻辑约束。

### 2. 智能参数优化层 (Parameter Architect Agent)
* **功能逻辑**：将抽象语义转译为高密度、高确定性的技术参数（包含体积光控制、骨相锚定值、材质属性等）。
* **优化目标**：通过对 Prompt 进行结构化重构，确保在不同视角下主体特征（人物、关键资产）的参数权重实现高度对齐。

### 3. 视觉一致性校验层 (Continuity Validator Agent)
* **功能逻辑**：基于 **ReAct 循环机制** 对多组分镜参数进行交叉比对。
* **闭环修复**：实时监测关键物品、角色面部结构、环境色温的逻辑冲突，并自动触发修正指令，实现“视觉协议”的一致性闭环。

## 技术栈
- **Orchestration**: CrewAI
- **LLM Engine**: GPT-4o / Claude 3.5 (Configurable)
- **Framework**: LangChain / Python