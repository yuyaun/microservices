# Microservice 範例

此專案示範使用 FastAPI 建立微服務，整合 Kafka MQ、Job 排程、PostgreSQL + SQLAlchemy + Alembic。

## 安裝依賴

```bash
python3 -m venv .venv
. .venv/bin/activate
pip3 install -r requirements.txt
```

## docker-compose 啟動

```bash
docker-compose up -d
```

## 啟動 FastAPI

```bash
 python3 -m uvicorn app.main:app --reload
```

## 啟動 Kafka 消費者

```bash
python3 -m app.mq.consumer
```

## 執行 Job（可搭配 cron）

```bash
python3 -m app.job.run
```


## Alembic 初始化

```bash
alembic init alembic
# env.py 會從 `.env` 讀取 DATABASE_URL
# 然後建立 migration
alembic revision --autogenerate -m "init"
alembic upgrade head
```
