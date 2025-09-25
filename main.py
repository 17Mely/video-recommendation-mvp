from fastapi import FastAPI

app = FastAPI()

@app.get("/feed")
def get_feed(username: str):
    # Placeholder recommendations
    return {"username": username, "recommendations": ["Video 1", "Video 2"]}

from sklearn.feature_extraction.text import TfidfVectorizer

videos = [
    {"title": "Cooking Pasta", "tags": "cooking food Italian"},
    {"title": "Python Basics", "tags": "programming python"},
    {"title": "Fitness Tips", "tags": "workout health"},
]
def recommend():
    corpus = [v["title"] + " " + v["tags"] for v in videos]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    # For MVP, return the top video titles
    return [v["title"] for v in videos]

@app.get("/feed")
def get_feed(username: str):
    recs = recommend()
    return {"username": username, "recommendations": recs}

