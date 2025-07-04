from pydantic import BaseSettings

class Settings(BaseSettings):
    # 組成 topic 名稱（格式為 `{ENV}.{object}.{action}`）
    # 建立與監控 consumer group（格式為 `{ENV}-{MICROSERVICE_NAME}`）
    kafka_bootstrap_servers: str = "localhost:9092"
    kafka_topic: str = "order.created"
    database_url: str = "postgresql://postgres:password@localhost:5432/postgres"

settings = Settings()