import streamlit as st
from src.content_based import get_recommendations
from src.item_cf import get_similar_movies
from src.hybrid import hybrid_recommend

from src.recommender import (
    get_recommendations,
    get_movie_list
)
st.set_page_config(
    page_title="Movie Recommendation System",
    layout="centered",
    initial_sidebar_state="auto"    

)

st.header("🎬 Movie Recommendation System")

st.caption(
    "Content-Based Recommendation Engine using MovieLens 1M Dataset"
)

st.write(
    "Content-Based Movie Recommendation Engine using MovieLens 1M Dataset"
)

selected_movie = st.selectbox(
    "Select a Movie",
    get_movie_list()
)

model_type = st.selectbox(
    "Recommendation Model",
    [
        "Content-Based",
        "Item-Based",
        "Hybrid"
    ]
)

if st.button("Recommend"):

    st.info(
        f"Using {model_type}"
    )

    if model_type == "Content-Based":

        recommendations = get_recommendations(
            selected_movie
        )

    elif model_type == "Item-Based":

        recommendations = get_similar_movies(
            selected_movie
        )["title"]

    else:

        recommendations = hybrid_recommend(
            selected_movie
        )

    st.subheader("Recommended Movies")

    for i, movie in enumerate(
        recommendations,
        start=1
    ):
        st.write(f"{i}. {movie}")