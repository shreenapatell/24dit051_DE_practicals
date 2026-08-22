import pandas as pd
import random
import time

users = ["Alice", "Bob", "Charlie", "David", "Emma"]

actions = ["Login", "Logout", "Purchase", "View", "Search"]

records = []

for i in range(10000):
    records.append({
        "timestamp": time.time(),
        "user": random.choice(users),
        "action": random.choice(actions),
        "cpu": round(random.uniform(10, 90), 2),
        "memory": round(random.uniform(20, 95), 2)
    })

df = pd.DataFrame(records)
df.to_csv("user_logs.csv", index=False)

print("Dataset created successfully!")