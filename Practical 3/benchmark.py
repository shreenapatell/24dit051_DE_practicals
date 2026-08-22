import pandas as pd
import matplotlib.pyplot as plt

comparison = {

    "Pipeline": [
        "Batch",
        "Realtime"
    ],

    "Latency(ms)": [
        1200,
        8
    ],

    "Throughput(records/sec)": [
        900,
        420
    ],

    "Fault Recovery(sec)": [
        15,
        3
    ]
}

df = pd.DataFrame(comparison)

print(df)

plt.figure(figsize=(6,4))
plt.bar(df["Pipeline"], df["Latency(ms)"])
plt.title("Latency Comparison")
plt.ylabel("Milliseconds")
plt.show()

plt.figure(figsize=(6,4))
plt.bar(df["Pipeline"], df["Throughput(records/sec)"])
plt.title("Throughput Comparison")
plt.ylabel("Records/sec")
plt.show()