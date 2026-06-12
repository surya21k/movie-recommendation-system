from surprise import Dataset
from surprise import Reader
from surprise import SVD

from src.data_loader import (
    load_movies,
    load_ratings
)
movies = load_movies()
ratings = load_ratings()
reader = Reader(
    rating_scale=(1, 5)
)

data = Dataset.load_from_df(
    ratings[
        ["userId", "movieId", "rating"]
    ],
    reader
)

trainset = data.build_full_trainset()
reader = Reader(
    rating_scale=(1, 5)
)

data = Dataset.load_from_df(
    ratings[
        ["userId", "movieId", "rating"]
    ],
    reader
)

trainset = data.build_full_trainset()
model = SVD()

model.fit(trainset)

def recommend_for_user(
    user_id,
    n=10
):
    pass