from kafka import KafkaConsumer
import json
import time

consumer = KafkaConsumer(
    "activity_logs",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("Listening for messages...")

for msg in consumer:
    data = msg.value
    latency = (time.time() - data["timestamp"]) * 1000

    print("--------------------------------")
    print(data)
    print("Latency:", round(latency, 2), "ms")