from confluent_kafka import Consumer
from app.core.config import settings
from app.mq.handlers.order_handler import handle_order_created

conf = {
    "bootstrap.servers": settings.kafka_bootstrap_servers,
    "group.id": settings.kafka_consumer_group,
    "auto.offset.reset": "earliest"
}

print(f"Connecting to Kafka at {settings.kafka_bootstrap_servers}...")

consumer = Consumer(conf)
consumer.subscribe([settings.kafka_topic])

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    handle_order_created(msg.value().decode("utf-8"))