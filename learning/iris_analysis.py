import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Load Iris dataset directly from URL
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# 1. Initial inspection
print("=== HEAD ===")
print(df.head())

print("\n=== INFO ===")
print(df.info())

print("\n=== DESCRIBE ===")
print(df.describe())

print("\n=== SHAPE ===")
print("Rows, Columns:", df.shape)

print("\n=== SPECIES COUNT ===")
print(df['species'].value_counts())

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

# 2. Group by species
print("\n=== AVG BY SPECIES ===")
print(df.groupby('species').mean(numeric_only=True))

# 3. Plot
df.groupby('species')['sepal_length'].mean().plot(kind='bar', color=['blue','green','red'])
plt.title('Avg Sepal Length by Species')
plt.ylabel('Sepal Length (cm)')
plt.tight_layout()
plt.savefig('iris_plot.png')
plt.close()
print("\n✅ iris_plot.png saved")
