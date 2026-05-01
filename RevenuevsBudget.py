import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# DATA LOAD
# Load the dataset and perform a quick check
df = pd.read_excel("movies.xlsx")

print("Dataset Preview:")
print(df.head())

print("\nColumns:")
print(df.columns)


# DATA PREPARATION
# Select relevant variables for analysis
df = df[['budget', 'revenue', 'popularity', 'vote_average', 'vote_count']]

# Remove missing values and unrealistic entries
df = df.dropna()
df = df[(df['budget'] > 0) & (df['revenue'] > 0)]

print("\nCleaned Data Shape:", df.shape)


# SCATTER PLOT
# Analyze relationship between budget and revenue
plt.figure(figsize=(8,6))
plt.scatter(df['budget'], df['revenue'], alpha=0.6)
plt.xlabel("Budget")
plt.ylabel("Revenue")
plt.title("Budget vs Revenue Relationship")
plt.grid(True)
plt.show()


# FEATURE IMPORTANCE VISUALIZATION
# Display importance values obtained from ML model
features = ['vote_count', 'budget', 'vote_average', 'popularity']
importance = [0.77, 0.18, 0.03, 0.009]

plt.figure(figsize=(8,6))
plt.bar(features, importance)
plt.title("Feature Importance from Decision Tree")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


# CORRELATION HEATMAP
# Show relationships between all variables
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix of Variables")
plt.show()