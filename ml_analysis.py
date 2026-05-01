import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score



df = pd.read_excel("movies.xlsx")

print("DATA LOADED")
print(df.head())



print("\nCOLUMNS:")
print(df.columns)



df = df[['budget', 'revenue', 'popularity', 'vote_average', 'vote_count']]


#CLEANING
df = df.dropna()
df = df[(df['budget'] > 0) & (df['revenue'] > 0)]

print("\nCLEANED DATA:", df.shape)



df['success'] = (df['revenue'] > df['budget']).astype(int)



#MODEL 1: LINEAR REGRESSION


X = df[['budget', 'popularity', 'vote_average', 'vote_count']]
y = df['revenue']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nLINEAR REGRESSION")
print("R2:", r2_score(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))



#MODEL 2: DECISION TREE

X = df[['budget', 'popularity', 'vote_average', 'vote_count']]
y = df['success']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

tree = DecisionTreeClassifier(max_depth=4)
tree.fit(X_train, y_train)

y_pred = tree.predict(X_test)

print("\nDECISION TREE")
print("Accuracy:", accuracy_score(y_test, y_pred))



#FEATURE IMPORTANCE

importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': tree.feature_importances_
})

print("\nFEATURE IMPORTANCE")
print(importance.sort_values(by='Importance', ascending=False))