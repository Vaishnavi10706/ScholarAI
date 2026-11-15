
from fastapi import FastAPI

app = FastAPI(
    title="ScholarAI API",
    description="AI-powered Research Assistant",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to ScholarAI!",
        "status": "running"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
