import json
import pandas as pd
import matplotlib.pyplot as plt

load_file = "../results/load.json"
stress_file = "../results/stress.json"
soak_file = "../results/soak.json"

def extract_count(filename):
    count = 0
    with open(filename) as f:
        for _ in f:
            count += 1
    return count

load_count = extract_count(load_file)
stress_count = extract_count(stress_file)
soak_count = extract_count(soak_file)

tests = ["Load", "Stress", "Soak"]
iterations = [load_count, stress_count, soak_count]

plt.figure()
plt.bar(tests, iterations)
plt.title("Total Requests Comparison")
plt.xlabel("Test Type")
plt.ylabel("Total Requests")
plt.savefig("requests_comparison.png")
plt.close()

print("Charts generated successfully!")
