import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from src.data_loader import (
    load_movies,
    load_ratings
)
movies = load_movies()
ratings = load_ratings()

# Create a user-item matrix
movie_user_matrix = ratings.pivot_table(
    index="movieId",
    columns="userId",
    values="rating"
)

movie_user_matrix = movie_user_matrix.fillna(0)

# calculate similarity between movies
movie_similarity = cosine_similarity(
    movie_user_matrix
)

movie_similarity_df = pd.DataFrame(
    movie_similarity,
    index=movie_user_matrix.index,
    columns=movie_user_matrix.index
)
movie_indices = pd.Series(
    movies["movieId"].values,
    index=movies["title"]
)

#Recommendation function
def get_similar_movies(
    movie_title,
    n=10
):

    movie_id = movie_indices[
        movie_title
    ]

    similarity_scores = (
        movie_similarity_df[movie_id]
        .sort_values(
            ascending=False
        )
    )

    similar_movie_ids = (
        similarity_scores.index[
            1:n+1
        ]
    )

    recommendations = movies[
        movies["movieId"].isin(
            similar_movie_ids
        )
    ]

    return recommendations[
        ["title", "genres"]
    ]
