import streamlit as st
import pickle
import requests
import pandas as pd
from dotenv import load_dotenv
from huggingface_hub import hf_hub_download
import os

load_dotenv()

api_key = os.getenv("TMDB_API_KEY")

files_to_download = ["movies_dict.pkl", "similarity.pkl"]

for filename in files_to_download:
    if not os.path.exists(filename):
        print(f"Downloading {filename} from Hugging Face...")
        hf_hub_download(
            repo_id="Dhamz10/movie-recommender-similarity",
            filename=filename,
            local_dir=".",
            repo_type='dataset',
            local_dir_use_symlinks=False,
        )

movies_list = pickle.load(open("movies_dict.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))
movies = pd.DataFrame(movies_list)


def fetch_poster(movie_id):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    )
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]


def recommend(movie):
    new_idx = movies[movies["title"] == movie].index[0]
    distances = similarity[new_idx]
    res = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommendations_posters = []

    for i in res:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        recommendations_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommendations_posters


st.title("Movies Recommender System")
selected_movie = st.selectbox(
    "Select a Movie: ",
    (movies["title"].values),
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
