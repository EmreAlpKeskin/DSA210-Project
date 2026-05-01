import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset
df = pd.read_excel("movies.xlsx")

# Prepare data
df = df[['budget', 'revenue']]
df = df.dropna()
df = df[(df['budget'] > 0) & (df['revenue'] > 0)]

print("Data ready:", df.shape)


# Hypothesis definition
print("\nHYPOTHESIS TEST")
print("H0: There is no relationship between budget and revenue.")
print("H1: There is a relationship between budget and revenue.")


# Pearson correlation test
corr, p_value = pearsonr(df['budget'], df['revenue'])

print("\nResults:")
print("Correlation:", corr)
print("P-value:", p_value)


# Decision
alpha = 0.05

if p_value < alpha:
    print("\nDecision: Reject H0")
    print("Conclusion: There is a statistically significant relationship between budget and revenue.")
else:
    print("\nDecision: Fail to reject H0")
    print("Conclusion: There is no statistically significant relationship.")


# Interpretation
print("\nInterpretation:")

if corr > 0:
    print("The relationship is positive. Higher budget movies tend to generate higher revenue.")
elif corr < 0:
    print("The relationship is negative.")
else:
    print("No clear linear relationship.")


# -----------------------------
# GRAPH 1: REVENUE DISTRIBUTION
# -----------------------------
plt.figure(figsize=(8, 6))

sns.histplot(df['revenue'], bins=50, kde=True)

plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.grid(True)

plt.show()


# -----------------------------
# GRAPH 2: BOXPLOT (SUCCESS vs BUDGET)
# -----------------------------

# Create success variable
df['success'] = (df['revenue'] > df['budget']).astype(int)

plt.figure(figsize=(8, 6))

sns.boxplot(
    x=df['success'],
    y=df['budget']
)

plt.title("Budget Distribution by Success")
plt.xlabel("Success (1 = Yes, 0 = No)")
plt.ylabel("Budget")
plt.grid(True)

plt.show()