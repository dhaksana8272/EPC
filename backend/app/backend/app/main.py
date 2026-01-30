# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router

# Create FastAPI app
app = FastAPI(
    title="EPC Reasoning Engine",
    description="Domain-specific EPC document reasoning system",
    version="1.0.0"
)

# Enable CORS (for React frontend or testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all during development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes under /api
app.include_router(api_router, prefix="/api")

# Health check endpoint
@app.get("/")
def root():
    return {
        "status": "running",
        "message": "EPC Reasoning Engine backend is live"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
