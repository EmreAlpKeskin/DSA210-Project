import pandas as pd
import matplotlib.pyplot as plt
import ast

# Load dataset
df = pd.read_csv("tmdb_5000_movies.csv")

# Keep only necessary columns
df = df[['genres', 'revenue', 'budget']]

# Remove missing values
df = df.dropna()

# Function to extract first genre
def extract_genre(genre_text):
    try:
        genre_list = ast.literal_eval(genre_text)

        if len(genre_list) > 0:
            return genre_list[0]['name']

        return "Unknown"

    except:
        return "Unknown"

# Create new genre column
df['main_genre'] = df['genres'].apply(extract_genre)

# Create success column
df['success'] = df['revenue'] > df['budget']


# GRAPH 1
# Movie count by genre


genre_counts = df['main_genre'].value_counts().head(10)

plt.figure(figsize=(10,6))

genre_counts.plot(kind='bar')

plt.title("Top 10 Movie Genres")
plt.xlabel("Genre")
plt.ylabel("Number of Movies")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("Genre_Counts.png")

plt.show()

# -----------------------------
# GRAPH 2
# Success rate by genre
# -----------------------------

genre_success = df.groupby('main_genre')['success'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))

genre_success.plot(kind='bar')

plt.title("Success Rate by Genre")
plt.xlabel("Genre")
plt.ylabel("Success Rate")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("Genre_Success_Rate.png")

plt.show()

# Print results
print("\nTop Genres:")
print(genre_counts)

print("\nSuccess Rates:")
print(genre_success)