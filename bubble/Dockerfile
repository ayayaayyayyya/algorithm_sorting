FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 요구사항 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY . .

# Gunicorn을 사용하여 Flask 앱 실행 (반드시 $PORT 사용)
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
