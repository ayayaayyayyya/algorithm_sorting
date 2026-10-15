import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# 1. 기본 접속 확인용 라우트 (GET / POST)
@app.route("/", methods=["GET", "POST"])
def index():
    # Apps Script에서 보낸 JSON 데이터 읽기
    data = request.get_json(silent=True) or {}
    
    # 전달받은 데이터 확인 로그 (Cloud Run 로그 탭에서 확인 가능)
    print(f"Received data: {data}")
    
    # 앱스 스크립트로 보낼 응답
    return jsonify({
        "status": "success",
        "message": "Cloud Run 서버 연결 성공!",
        "received_data": data
    }), 200

# 2. 추가 API 요청용 라우트 (필요시 사용)
@app.route("/api", methods=["POST"])
def handle_api():
    data = request.get_json(silent=True) or {}
    
    return jsonify({
        "status": "success",
        "result": "API 요청 처리 완료",
        "payload": data
    }), 200

# 3. Cloud Run 포트 및 호스트 바인딩 설정
if __name__ == "__main__":
    # Cloud Run은 PORT 환경변수로 8080 포트를 할당합니다.
    port = int(os.environ.get("PORT", 8080))
    # 외부 요청 수신을 위해 host='0.0.0.0' 바인딩 필수
    app.run(host="0.0.0.0", port=port)
