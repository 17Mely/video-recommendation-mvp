from fastapi import FastAPI

app = FastAPI()

@app.get("/feed")
def get_feed(username: str):
    # Placeholder recommendations
    return {"username": username, "recommendations": ["Video 1", "Video 2"]}
