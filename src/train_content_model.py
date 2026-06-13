from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import joblib

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

joblib.dump(
    cosine_sim,
    "models/cosine_sim.pkl"
)

joblib.dump(
    indices,
    "models/indices.pkl"
)

print("Content-based model saved successfully!")