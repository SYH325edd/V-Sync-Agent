from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app) # 允许网页跨域访问

@app.route('/run-agent', methods=['POST'])
def run_agent():
    try:
        # 这里的命令相当于你在 CMD 输入 python main.py
        result = subprocess.run(['python', 'main.py'], capture_output=True, text=True)
        return jsonify({"status": "success", "output": result.stdout})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(port=5000) # 本地监听 5000 端口