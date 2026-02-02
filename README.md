.

# 🎬 Movie Recommender System

A content-based movie recommendation system built using Machine Learning and deployed as a Streamlit web app on Render.

## 📌 Features

🔍 Search for a movie and get similar movie recommendations

🎭 Uses movie metadata (genres, keywords, overview, cast, crew)

📊 Machine Learning with cosine similarity

🖼 Fetches posters using TMDB API

☁️ Deployed on Render

🔐 Secure API key handling using environment variables

📦 Large ML models managed with Git LFS


## 🛠 Tech Stack

Frontend / UI: Streamlit

Backend / ML: Python, Scikit-learn

Data Handling: Pandas, NumPy

Model Storage: Pickle (.pkl)

Deployment: Render

Version Control: Git & GitHub (Git LFS - for large ML artifacts)

## 📂 Project Structure

movie_recommender/
│
├── app.py                  # Streamlit application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│── movie_list.pkl          # Processed movie dataset
│── similarity.pkl          # Cosine similarity matrix
└── .gitignore


## 🧠 How It Works (Simple Explanation)

Movie metadata is combined into a single tags column

Text data is vectorized using CountVectorizer

Cosine similarity is used to find similar movies

When a user selects a movie, the system recommends the top similar movies

Think of it like: movies with similar words → similar vectors → similar recommendations


## 🚀 Run Locally
### 1️⃣ Clone the repository
git clone https://github.com/MujKumail/movie-recommender.git
cd movie-recommender

### 2️⃣ Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Run the app
streamlit run app.py

## 🌐 Deployment

The application is deployed on Render using GitHub integration and environment variables for secure configuration.
