import csv
import random
from datetime import datetime, timedelta

users = ["user1", "user2", "user3", "user4", "user5"]
actions = ["login", "view", "search", "purchase", "logout"]

start_time = datetime.now()

with open("activity_logs.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "user", "action", "response_time_ms"])

    for i in range(10000):
        timestamp = start_time + timedelta(seconds=i)
        user = random.choice(users)
        action = random.choice(actions)
        response_time = random.randint(50, 1000)

        writer.writerow([
            timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            user,
            action,
            response_time
        ])

print("Generated 1000 activity log records.")