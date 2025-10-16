# 🎬 Movie Recommender (Content-Based, Streamlit)

This interactive app suggests movies that are most similar to the one you choose. It analyzes each film’s genre, cast, director, and short summary to find the closest matches and shows their posters instantly.
The app uses content-based filtering, meaning it focuses on movie attributes instead of user ratings or watch history.
Built with **Python** and **Streamlit**, this demo runs inside a **Docker** container and uses the TMDB to display movie posters.

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

