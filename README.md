# 🎬 Movie Recommender (Content-Based, Streamlit)

A simple, fast movie recommender that suggests **Top-5 similar films** using content features (genres, cast, director, overview text) and **cosine similarity**. Built with **Streamlit** and uses **TMDB** for posters.

---

## ✨ What it does

- Pick a movie from the dropdown
- Computes similarity to all other movies
- Shows **five most similar** titles + posters (via TMDB)

---

## 🧠 How it works (high level)

1. **Text features** are assembled into a `tags` field (genres + top cast + director + processed overview).
2. `CountVectorizer` converts `tags` into vectors (bag-of-words).
3. **Cosine similarity** measures how close movies are in that vector space.
4. For the selected movie, the app returns the **nearest neighbors**.

> Cosine similarity compares **angles**, so two descriptions with the same mix of terms match even if one is longer.

---

