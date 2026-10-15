
FROM python:3.11-slim

# 작업 디렉터리 설정
WORKDIR /app

# 의존성 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 전체 소스 코드 복사 (main.py 등 포함)
COPY . .

# Cloud Run 기본 포트(8080) 환경변수 및 실행 명령
ENV PORT 8080
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
