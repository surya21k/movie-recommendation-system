import requests
import streamlit as st
import re


@st.cache_data
def fetch_poster(movie_name):

    try:

        # Remove year
        movie_name = re.sub(r"\(\d{4}\)", "", movie_name).strip()

        # Fix MovieLens naming
        movie_name = movie_name.replace(", The", "")
        movie_name = movie_name.replace(", A", "")
        movie_name = movie_name.replace(", An", "")

        api_key = st.secrets["TMDB_API_KEY"]

        response = requests.get(
            "https://api.themoviedb.org/3/search/movie",
            params={
                "api_key": api_key,
                "query": movie_name
            },
            timeout=5
        )

        if response.status_code != 200:
            return None

        data = response.json()

        if not data.get("results"):
            return None

        poster_path = data["results"][0].get("poster_path")

        if not poster_path:
            return None

        return (
            f"https://image.tmdb.org/t/p/w500{poster_path}"
        )

    except Exception:
        return None