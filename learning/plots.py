import matplotlib.pyplot as plt
import numpy as np

# Histogram
data = np.random.randn(1000)

plt.figure(figsize=(8,5))
plt.hist(data, bins=30)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.grid(True)
plt.savefig("histogram.png")
plt.close()

print("Histogram saved")

# Pie chart
labels = ["Python", "JavaScript", "C++", "Java"]
sizes = [40, 30, 15, 15]

plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Programming Languages")
plt.savefig("pie_chart.png")
plt.close()

print("Pie chart saved")