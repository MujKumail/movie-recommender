import os
import pickle
import streamlit as st
import requests
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
from dotenv import load_dotenv
load_dotenv()


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.movie-card {
    background-color: #1c1f26;
    padding: 10px;
    border-radius: 16px;
    transition: transform 0.4s;
}

.movie-card:hover {
    transform: scale(1.08);
}

.movie-poster {
    width: 100%;
    border-radius: 12px;
}

.movie-title {
    font-size: 15px;
    font-weight: 600;
    color: white;
    margin-top: 8px;
    height: 42px;
    overflow: hidden;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
}

.rating {
    background: #f5c518;
    color: black;
    font-weight: bold;
    padding: 3px 8px;
    border-radius: 8px;
    font-size: 13px;
    display: inline-block;
    margin-top: 6px;
}

.genre {
    display: inline-block;
    background: #333;
    color: #ccc;
    font-size: 12px;
    padding: 2px 6px;
    border-radius: 6px;
    margin: 3px 3px 0 0;
}
</style>
""", unsafe_allow_html=True)

# ---------------- FUNCTIONS ----------------
def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    data = requests.get(url).json()

    poster_path = data.get("poster_path")
    poster = (
        "https://image.tmdb.org/t/p/w500/" + poster_path
        if poster_path else
        "https://via.placeholder.com/500x750?text=No+Image"
    )

    rating = round(data.get("vote_average", 0), 1)
    genres = [g["name"] for g in data.get("genres", [])][:2]

    return poster, rating, genres


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommendations = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        title = movies.iloc[i[0]].title
        poster, rating, genres = fetch_movie_details(movie_id)

        recommendations.append({
            "title": title,
            "poster": poster,
            "rating": rating,
            "genres": genres
        })

    return recommendations


# ---------------- LOAD DATA ----------------
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# ---------------- HEADER ----------------
st.markdown("<h1 style='text-align:center;'>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color:gray;'>Find movies similar to your favorite one</p>",
    unsafe_allow_html=True
)


# ---------------- MOVIE SELECT ----------------
movie_list = movies['title'].values
selected_movie = st.selectbox("🎥 Select a Movie", movie_list)

# ---------------- BUTTON ----------------
if st.button("✨ Show Recommendations"):
    with st.spinner("Fetching recommendations..."):
        recs = recommend(selected_movie)

    cols = st.columns(5)

    for col, movie in zip(cols, recs):
        with col:
            genres_html = "".join(
                [f"<span class='genre'>{g}</span>" for g in movie["genres"]]
            )

            st.markdown(f"""
            <div class="movie-card">
                <img src="{movie['poster']}" class="movie-poster">
                <div class="movie-title" title="{movie['title']}">
                    {movie['title']}
                </div>
                <div class="rating">⭐ {movie['rating']}</div>
                <div>{genres_html}</div>
            </div>
            """, unsafe_allow_html=True)




