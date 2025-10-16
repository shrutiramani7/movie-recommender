import streamlit as st
import pickle
import requests
import os
from dotenv import load_dotenv
import joblib

load_dotenv()

TMDB_API_KEY = os.environ.get("TMDB_API_KEY")

def fetch_poster(movie_id):
    response = requests.get(
    f"https://api.themoviedb.org/3/movie/{movie_id}",
    params={"api_key": TMDB_API_KEY, "language": "en-US"},
    timeout=10
)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # Fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

with open("artifacts/movies.pkl","rb") as f:
    movies = pickle.load(f)
similarity = joblib.load("artifacts/similarity.joblib")


st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button("Recommend", type="primary"):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)
    for col, name, poster in zip(cols, names, posters):
        with col:
            st.image(poster, use_column_width=True)
            st.markdown(f"**{name}**")