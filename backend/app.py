from fastapi import FastAPI

from backend.routes import router

app = FastAPI(
    title="Enterprise AI Copilot",
    description="RAG-based AI Assistant using Gemini and ChromaDB",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Enterprise AI Copilot 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


app.include_router(router)