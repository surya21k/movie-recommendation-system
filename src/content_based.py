from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

from src.data_loader import load_movies

movies = load_movies()

tfidf = TfidfVectorizer(
    stop_words="english"
)

tfidf_matrix = tfidf.fit_transform(
    movies["genres"]
)

cosine_sim = cosine_similarity(
    tfidf_matrix
)

indices = pd.Series(
    movies.index,
    index=movies["title"]
).drop_duplicates()


def get_recommendations(
    title,
    n=10
):

    idx = indices[title]

    similarity_scores = list(
        enumerate(
            cosine_sim[idx]
        )
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    similarity_scores = similarity_scores[
        1:n+1
    ]

    movie_indices = [
        i[0]
        for i in similarity_scores
    ]

    return movies[
        "title"
    ].iloc[
        movie_indices
    ]