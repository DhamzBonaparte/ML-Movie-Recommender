# 🎬 Movie Recommender System

A content-based movie recommendation web application built with **Python**, **Streamlit**, and **Scikit-Learn**. It suggests similar movies based on user selection and fetches real-time movie posters using the **TMDB API**.

🔗 **Live Demo:** [https://ml-movie-recommender-muum.onrender.com/](https://ml-movie-recommender-muum.onrender.com/)

---

## 🚀 Features
* **Content-Based Filtering:** Uses cosine similarity on movie metadata (genres, cast, crew, overview) to find matching titles.
* **Interactive UI:** Built using Streamlit for a fast, clean, and responsive user interface.
* **Dynamic Posters:** Integrates with the TMDB API to pull high-quality official movie posters for recommendations.
* **Cloud-Optimized Architecture:** Large dataset and similarity model matrices are hosted externally on Hugging Face to ensure a lightweight and seamless deployment.

---

## 🛠️ Tech Stack
* **Frontend/UI:** Streamlit
* **Data Processing & ML:** Pandas, NumPy, Scikit-Learn, Pickle
* **API Integration:** TMDB (The Movie Database) API
* **Cloud Storage:** Hugging Face Datasets (for large `.pkl` files)
* **Deployment:** Render

---

## 📂 Project Structure
```text
├── .gitignore               # Files and folders to ignore by Git
├── app.py                   # Main Streamlit application and download logic
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation