import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv("data.csv")

# Basic info
print(df.head())
print(df.describe())

# Average example column (replace Salary with your column name)
print("Average Salary:", df["Salary"].mean())

# Group by Department
print(df.groupby("Department")["Salary"].mean())

# Bar chart
df.groupby("Department")["Salary"].mean().plot(kind="bar")
plt.title("Average Salary by Department")
plt.show()

# Scatter plot
plt.scatter(df["Age"], df["Salary"])
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

# Heatmap
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()
