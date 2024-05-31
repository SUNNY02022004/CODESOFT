import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
dataset_path = "C:\\Users\\kiran\\Desktop\\codesoft\\Recommendation Project\\anime.csv"
anime_data = pd.read_csv(dataset_path)

# Drop rows with missing values
anime_data.dropna(inplace=True)

# Convert genre column to list of genres
anime_data['genre'] = anime_data['genre'].apply(lambda x: x.split(', '))

# Function to preprocess genre data
def preprocess_genre(genres):
    return ' '.join(genres)

# Apply preprocessing to the genre column
anime_data['processed_genre'] = anime_data['genre'].apply(preprocess_genre)

# Function to create a user-anime matrix
def create_user_anime_matrix(data):
    user_anime_matrix = data.pivot_table(index='name', columns='anime_id', values='rating').fillna(0)
    return user_anime_matrix

# Create user-anime matrix
user_anime_matrix = create_user_anime_matrix(anime_data)

# Compute cosine similarity between anime
anime_similarity = cosine_similarity(user_anime_matrix)

# Convert to DataFrame for better readability
anime_similarity_df = pd.DataFrame(anime_similarity, index=user_anime_matrix.index, columns=user_anime_matrix.index)

# Function to get recommendations
def get_recommendations(anime_name, anime_similarity_df, top_n=5):
    recommendations = anime_similarity_df[anime_name].sort_values(ascending=False).head(top_n+1)
    recommendations = recommendations.drop(anime_name)
    return recommendations

# Example usage
anime_name = "Kimi no Na wa."
top_n = 5
recommendations = get_recommendations(anime_name, anime_similarity_df, top_n)
print(f"Top {top_n} recommended anime for '{anime_name}':\n", recommendations)
