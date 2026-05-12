import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "students": ["Ali", "Ahmed", "Muzammil", "Usama", "Zain", "Bilal", "Zaib", "Qasim","Hussain", "Usman"],
    "age": [25, 30, 22, 28, 32, 27, 24, 26, 29, 35],
    "city": ["Lahore", "Karachi", "Faisalabad", "Islamabad", "Lahore", "Karachi", "Faisalabad", "Islamabad", "Lahore", "Karachi"],
    "marks": [76,43,64,87,56,45,65,34,65,65],
    "study_hours": [2,4,5,7,2,8,3,8,2,7]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Check null values
print("Average Marks")
print(df["marks"].mean())

print("highest marks")
print(df["marks"].max())

print("Students with marks > 70:")
print(df[df["marks"] > 70])

plt.figure(figsize=(8,5))
plt.scatter(df["study_hours"], df["marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(True)
plt.savefig("scatter_plot.png")
plt.close()