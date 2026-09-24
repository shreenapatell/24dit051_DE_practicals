import csv
import json
import time
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

topic = "activity_logs"

with open("activity_logs.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        producer.send(topic, row)
        print(f"Sent: {row}")
        time.sleep(0.01)

producer.flush()
producer.close()

print("All records sent successfully.")