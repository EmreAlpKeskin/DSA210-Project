import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset
df = pd.read_excel("movies.xlsx")

# Prepare data
df = df[['budget', 'revenue']]
df = df.dropna()
df = df[(df['budget'] > 0) & (df['revenue'] > 0)]

# Define success
df['success'] = (df['revenue'] > df['budget']).astype(int)


# Basic stats
print("Counts:")
print(df['success'].value_counts())

print("\nPercentages:")
print(df['success'].value_counts(normalize=True))


# Create figure with subplots
fig, axes = plt.subplots(1, 2, figsize=(12,5))


# Plot 1: Countplot
sns.countplot(x=df['success'], ax=axes[0])
axes[0].set_title("Successful vs Unsuccessful Movies")
axes[0].set_xlabel("Success (1 = Yes, 0 = No)")
axes[0].set_ylabel("Count")


# Add labels to bars
for i, count in enumerate(df['success'].value_counts().sort_index()):
    axes[0].text(i, count + 10, str(count), ha='center')


# Plot 2: Pie chart (extra visual)
labels = ['Unsuccessful', 'Successful']
values = df['success'].value_counts().sort_index()

axes[1].pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
axes[1].set_title("Success Distribution")


# Adjust layout
plt.tight_layout()

# Show both plots
plt.show()


# Extra comparison (numerical)
avg_budget = df.groupby('success')['budget'].mean()
avg_revenue = df.groupby('success')['revenue'].mean()

print("\nAverage Budget:")
print(avg_budget)

print("\nAverage Revenue:")
print(avg_revenue)