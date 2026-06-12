import streamlit as st
from src.content_based import get_recommendations
from src.item_cf import get_similar_movies
from src.hybrid import hybrid_recommend
from src.utils import fetch_poster

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
    for movie in recommendations[:5]:

        poster_url = fetch_poster(movie)

        col1, col2 = st.columns([1, 3])

        with col1:

            if poster_url:
                st.image(
                    poster_url,
                    width=150
                )
            else:
                st.markdown(
                    """
                    <div style="
                      width:150px;
                        height:225px;
                        background: linear-gradient(145deg, #1a2632, #0d1219);
                        border-radius: 12px;
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        justify-content: center;
                        box-shadow: 0 8px 16px -6px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.08);
                        border: 1px solid rgba(255,200,120,0.3);
                    ">
                        No Poster
                    </div>
                    """,
                unsafe_allow_html=True
                )

        with col2:

            st.markdown(
                f"### {movie}"
            )

        st.divider()