import jsonlines
import matplotlib.pyplot as plt
import os

os.makedirs("charts", exist_ok=True)

results_files = [
    "results/load_test.json",
    "results/stress_test.json",
    "results/soak_test.json"
]

test_names = ["Load Test", "Stress Test", "Soak Test"]

avg_response_times = []
throughputs = []
error_rates = []

for file in results_files:
    durations = []
    total_reqs = 0
    failed_reqs = 0

    with jsonlines.open(file) as reader:
        for entry in reader:
            if entry.get("type") == "Point":
                metric_name = entry.get("metric")
                value = entry["data"]["value"]
                if metric_name == "http_req_duration":
                    durations.append(value)
                elif metric_name == "http_reqs":
                    total_reqs += value
                elif metric_name == "checks":
                    failed_reqs += value

    avg_response_times.append(sum(durations)/len(durations) if durations else 0)
    throughputs.append(total_reqs)
    error_rates.append((failed_reqs/total_reqs)*100 if total_reqs > 0 else 0)

# Plot charts
plt.figure(figsize=(8,5))
plt.bar(test_names, avg_response_times, color='skyblue')
plt.ylabel("Average Response Time (ms)")
plt.title("K6 Test Response Times")
plt.savefig("charts/response_time.png")
plt.close()

plt.figure(figsize=(8,5))
plt.bar(test_names, throughputs, color='orange')
plt.ylabel("Total Requests")
plt.title("K6 Test Throughput")
plt.savefig("charts/throughput.png")
plt.close()

plt.figure(figsize=(8,5))
plt.bar(test_names, error_rates, color='red')
plt.ylabel("Error Rate (%)")
plt.title("K6 Test Error Rate")
plt.savefig("charts/error_rate.png")
plt.close()

print("Charts saved in charts/")

