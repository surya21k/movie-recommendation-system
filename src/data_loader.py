import pandas as pd

def load_movies():
    return pd.read_csv(
        "data/raw/movies.dat",
        sep="::",
        engine="python",
        encoding="latin-1",
        names=["movieId","title","genres"]
    )

def load_ratings():
    return pd.read_csv(
        "data/raw/ratings.dat",
        sep="::",
        engine="python",
        names=["userId","movieId","rating","timestamp"]
    )

def load_users():
    return pd.read_csv(
        "data/raw/users.dat",
        sep="::",
        engine="python",
        names=["userId","gender","age","occupation","zipCode"]
    )