import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
movies = pd.read_csv(
    r"C:\surya\ml\Movie-Recommendation-System\data\raw\movies.dat",
    sep="::",
    engine="python",
    encoding="latin-1",
    names=["movieId", "title", "genres"]
)

# TF-IDF
tfidf = TfidfVectorizer(stop_words="english")

tfidf_matrix = tfidf.fit_transform(
    movies["genres"]
)

# Cosine Similarity
cosine_sim = cosine_similarity(
    tfidf_matrix
)

# Movie lookup
indices = pd.Series(
    movies.index,
    index=movies["title"]
).drop_duplicates()


def get_recommendations(title, n=10):

    idx = indices[title]

    similarity_scores = list(
        enumerate(cosine_sim[idx])
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    similarity_scores = similarity_scores[1:n+1]

    movie_indices = [
        i[0]
        for i in similarity_scores
    ]

    return movies["title"].iloc[movie_indices]


def get_movie_list():
    return movies["title"].tolist()