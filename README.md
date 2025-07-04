# MyService Microservice 範例

此專案示範使用 FastAPI 建立微服務，整合 Kafka MQ、Job 排程、PostgreSQL + SQLAlchemy + Alembic。

## 啟動 FastAPI
```bash
uvicorn app.main:app --reload
```

## 啟動 Kafka 消費者
```bash
python app/mq/consumer.py
```

## 執行 Job（可搭配 cron）
```bash
python app/job/run.py
```

## Alembic 初始化
```bash
alembic init alembic
# 修改 alembic.ini 與 env.py 指向 app.core.database:Base
# 然後建立 migration
alembic revision --autogenerate -m "init"
alembic upgrade head
```