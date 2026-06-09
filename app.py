import streamlit as st

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

if st.button("Recommend"):

    st.success(
        f"You selected: {selected_movie}"
    )

    recommendations = get_recommendations(
        selected_movie
    )

    st.subheader("Recommended Movies")

    for i, movie in enumerate(
        recommendations,
        start=1
    ):
        st.write(f"{i}. {movie}")