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
CRON_JOB=true python3 -m uvicorn app.main:app --reload  # 若需同時啟動排程器
```

## 啟動 Kafka 消費者

```bash
python3 -m app.mq.consumer
```

## 執行單一 Job

```bash
python3 -m app.job.jobs.cleanup_order  # 或其他 job
```

## 啟動排程器

排程器會依 `app/job/scheduler.py` 中設定的 Cron 規則執行工作。

```bash
python3 -m app.job.scheduler
```

## Alembic 初始化

```bash
alembic init alembic
# env.py 會從 `.env` 讀取 DATABASE_URL
# 然後建立 migration
alembic revision --autogenerate -m "init"
alembic upgrade head
```

## 使用 Codex 生成程式碼

```bash
export OPENAI_API_KEY=your_openai_api_key
docker exec -it dev-python zsh
codex -a never "{PROMPT}"
```
