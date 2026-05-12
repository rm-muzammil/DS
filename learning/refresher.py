import numpy as np

# 1. Creating arrays
a = np.array([1, 2, 3, 4, 5])
b = np.zeros((3, 3))
c = np.arange(0, 10, 2)
d = np.linspace(0, 1, 5)

print("1D array:", a)
print("Zeros matrix:\n", b)
print("Arange:", c)
print("Linspace:", d)

# 2. Array operations
print("\nShape:", a.shape)
print("Dtype:", a.dtype)
print("Sum:", a.sum())
print("Mean:", a.mean())

# 3. Slicing
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("\nMatrix:\n", matrix)
print("First row:", matrix[0])
print("Last column:", matrix[:, -1])
print("Submatrix:\n", matrix[0:2, 0:2])

# 4. Broadcasting
print("\nMultiply by 2:", a * 2)
print("Add arrays:", a + np.array([10,20,30,40,50]))

import pandas as pd

# 1. Creating DataFrames
data = {
    'name': ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Usman'],
    'age': [25, 30, 22, 28, 35],
    'city': ['Lahore', 'Karachi', 'Faisalabad', 'Islamabad', 'Lahore'],
    'salary': [50000, 80000, 45000, 70000, 90000]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# 2. Basic info
print("\nShape:", df.shape)
print("\nInfo:")
print(df.dtypes)
print("\nDescribe:\n", df.describe())

# 3. Selecting data
print("\nNames column:", df['name'].values)
print("\nFirst 2 rows:\n", df.head(2))
print("\nSelect by index:\n", df.iloc[1:3])

# 4. Filtering
print("\nSalary > 60000:\n", df[df['salary'] > 60000])
print("\nFrom Lahore:\n", df[df['city'] == 'Lahore'])

# 5. Groupby
print("\nAvg salary by city:\n", df.groupby('city')['salary'].mean())

# 6. Adding column
df['senior'] = df['age'] > 28
print("\nWith senior column:\n", df)