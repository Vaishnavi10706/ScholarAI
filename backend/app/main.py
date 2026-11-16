from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import papers

app = FastAPI(
    title="ScholarAI API",
    description="AI-powered Research Assistant",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(papers.router)
@app.get("/")
def home():
    return {
        "message": "Welcome to ScholarAI!",
        "status": "running"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
