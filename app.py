import streamlit as st
from src.recommender import get_movie_list
from src.content_based import get_recommendations
from src.item_cf import get_similar_movies
from src.hybrid import hybrid_recommend
from src.utils import fetch_poster

st.set_page_config(
page_title="Movie Recommendation System",
page_icon="🎬",
layout="centered",
)
def get_movie_genre(movie_name):

    try:

        from src.content_based import movies

        genre = movies[
            movies["title"] == movie_name
        ]["genres"].values

        if len(genre) > 0:
            return genre[0]

    except:
        pass

    return "Unknown"

st.markdown("""
<style>

.movie-card {

    background:#161B22;
    border-radius:16px;
    padding:12px;
    margin-bottom:20px;

    box-shadow:
        0 4px 12px rgba(0,0,0,.4);

    transition:0.3s;
}

.movie-card:hover {

    transform:translateY(-5px);
}

.genre {

    color:#FFB84D;

    font-size:13px;

    font-weight:600;

    min-height:40px;
}

.movie-name {

    color:white;
    
    align-items:center;

    font-size:16px;

    font-weight:bold;

    min-height:60px;

    margin-top:10px;
}

.poster {

    border-radius:12px;

    overflow: ;
}

</style>
""",
unsafe_allow_html=True)
st.markdown("""

<h1 style='text-align:center;'>
🎬 Movie Recommendation System
</h1>

<h4 style='text-align:center;color:gray;'>
Hybrid Movie Recommendation Engine
</h4>
""", unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🎬 Movies", "3,883")

with col2:
    st.metric("👥 Users", "6,040")

with col3:
    st.metric("⭐ Ratings", "1M+")

st.divider()

with st.sidebar:
    st.title("⚙️ Controls")

selected_movie = st.selectbox(
    "Select Movie",
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

recommend_btn = st.button(
    "🎯 Recommend Movies"
)

st.markdown("---")

st.markdown(""" select a movie and the recommendation model you want to use. Then click the "Recommend Movies" button to see your personalized movie recommendations! """, unsafe_allow_html=True)

if recommend_btn:

 st.success(
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

st.subheader("🍿 Recommended Movies")

movies_to_show = recommendations[:6]

for row in range(0, 6, 3):

    cols = st.columns(3)

    for col, movie in zip(
        cols,
        movies_to_show[row:row+3]
    ):

        with col:

            poster_url = fetch_poster(movie)

            genre = get_movie_genre(movie)

            st.markdown(
                f"""
                <div class="movie-card" style="text-align:center;">

                <div class="genre">
                {genre}
                </div>

                """,
                unsafe_allow_html=True
            )

            if poster_url:

                st.markdown(
                    f"""
                    <div class="poster">
                    <img
                        src="{poster_url}"
                        style="
                        width:100%;
                        height:320px;
                        object-fit: auto;
                        border-radius:12px;
                        "
                    >
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    """
                    <div style="
                        height:320px;
                        background:linear-gradient(135deg, #1E1E1E, #2C2C2C);
                        border-radius:12px;
                        display:flex;
                        align-items:center;
                        justify-content:center;
                        color:white;
                    ">
                        No Poster
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.markdown(
                f"""
                <div class="movie-name" style="text-align:center;">
                
                {movie}
                </div>

                </div>
                """,
                unsafe_allow_html=True
            )