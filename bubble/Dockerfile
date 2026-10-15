FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PORT=8080

# requirements.txt를 복사하는 대신 필요한 패키지를 직접 명시해서 설치합니다.
RUN pip install --no-cache-dir Flask==3.0.3 gunicorn==22.0.0

COPY . .

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 main:app
