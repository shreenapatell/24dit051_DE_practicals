import json
import time
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "activity_logs",
    bootstrap_servers="localhost:9092",
    group_id="batch_group",
    auto_offset_reset="earliest",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

batch_size = 100
batch = []
total_processed = 0
start_time = time.time()

print("Batch consumer started...")

try:
    for message in consumer:
        batch.append(message.value)

        if len(batch) >= batch_size:
            print(f"Processing batch of {len(batch)} records...")
            time.sleep(0.2)

            total_processed += len(batch)
            print(f"Total processed: {total_processed}")

            batch.clear()

        if total_processed >= 1000:
            break

except KeyboardInterrupt:
    print("Batch consumer stopped.")

finally:
    consumer.close()

elapsed = time.time() - start_time
print(f"Processed {total_processed} records in {elapsed:.2f} seconds.")