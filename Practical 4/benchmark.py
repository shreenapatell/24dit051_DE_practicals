import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Pipeline": ["Batch", "Realtime"],
    "Latency(ms)": [1200, 8],
    "Throughput(records/sec)": [900, 420],
    "Fault Recovery(sec)": [15, 3]
}

df = pd.DataFrame(data)

print("\nPerformance Comparison:")
print(df)

# Latency
plt.figure()
plt.bar(df["Pipeline"], df["Latency(ms)"])
plt.title("Latency Comparison")
plt.xlabel("Pipeline")
plt.ylabel("Latency (ms)")
plt.tight_layout()
plt.savefig("latency_comparison.png")
plt.show()

# Throughput
plt.figure()
plt.bar(df["Pipeline"], df["Throughput(records/sec)"])
plt.title("Throughput Comparison")
plt.xlabel("Pipeline")
plt.ylabel("Records per Second")
plt.tight_layout()
plt.savefig("throughput_comparison.png")
plt.show()

# Fault Recovery
plt.figure()
plt.bar(df["Pipeline"], df["Fault Recovery(sec)"])
plt.title("Fault Recovery Comparison")
plt.xlabel("Pipeline")
plt.ylabel("Recovery Time (seconds)")
plt.tight_layout()
plt.savefig("fault_recovery_comparison.png")
plt.show()

print("\nGraphs saved successfully.")