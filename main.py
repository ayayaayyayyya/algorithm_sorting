import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    try:
        data = request.get_json(silent=True) or {}
        print(f"Received data: {data}")
        
        return jsonify({
            "status": "success",
            "message": "Cloud Run 서버 연결 성공!",
            "received_data": data
        }), 200
    except Exception as e:
        print(f"Error handling request: {str(e)}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route("/api", methods=["POST"])
def handle_api():
    try:
        data = request.get_json(silent=True) or {}
        return jsonify({
            "status": "success",
            "result": "API 요청 처리 완료",
            "payload": data
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
