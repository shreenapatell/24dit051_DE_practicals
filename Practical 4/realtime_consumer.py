import json
import time
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "activity_logs",
    bootstrap_servers="localhost:9092",
    group_id="realtime_group",
    auto_offset_reset="earliest",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

print("Real-time consumer started...")

count = 0
start_time = time.time()

try:
    for message in consumer:
        print(
            f"Partition: {message.partition} | "
            f"Offset: {message.offset} | "
            f"Data: {message.value}"
        )

        count += 1

        if count >= 1000:
            break

except KeyboardInterrupt:
    print("Consumer stopped.")

finally:
    consumer.close()

elapsed = time.time() - start_time
print(f"Processed {count} records in {elapsed:.2f} seconds.")