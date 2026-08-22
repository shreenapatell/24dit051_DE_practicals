from kafka import KafkaConsumer
import pandas as pd
import json

consumer = KafkaConsumer(
    "activity_logs",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

batch = []
BATCH_SIZE = 100

print("Waiting for batch...")

for message in consumer:
    batch.append(message.value)

    if len(batch) >= BATCH_SIZE:
        df = pd.DataFrame(batch)

        print("\nBatch Received")
        print(df.head())

        print("Records Processed:", len(batch))

        batch = []