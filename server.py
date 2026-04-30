import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

# ==========================================
# 核心配置
# ==========================================
ARK_API_KEY = "ark-4a6d7010-d649-4799-ade7-a81ab99a909d-51290"
ENDPOINT_ID = "ep-20260430112948-v88j8"

client = OpenAI(
    api_key = ARK_API_KEY,
    base_url = "https://ark.cn-beijing.volces.com/api/v3",
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def serve_index():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/api/run-agent', methods=['POST'])
def process_agent():
    try:
        data = request.get_json()
        user_script = data.get('script', '').strip()
        selected_mode = data.get('mode', 'storyboard_grid') 

        # 注入大师级灵魂指令
        master_prefix = "你是一个世界顶级的分镜师、导演、摄影师、演员、后期师。请将以下内容生成一个具有美感、设计感的3*3分镜图提示词。"
        
        mode_prompts = {
            "storyboard_grid": f"{master_prefix} 必须严格生成9个分镜。格式要求：直接从 1. 开始写到 9. ，每个序号后加描述。严禁使用*或#号，严禁任何废话。",
            "text2img": f"{master_prefix} 请直接生成一段极具视觉冲击力的文生图提示词。",
            "img2video": f"{master_prefix} 请生成一段充满张力的图生视频动态描述。"
        }

        completion = client.chat.completions.create(
            model = ENDPOINT_ID,
            messages = [
                {"role": "system", "content": mode_prompts.get(selected_mode)},
                {"role": "user", "content": user_script},
            ],
        )

        # 清洗掉所有干扰符号
        final_result = completion.choices[0].message.content.replace("*", "").replace("#", "").replace("[", "").replace("]", "")
        
        return jsonify({"status": "success", "result": final_result}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=False)