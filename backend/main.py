from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
app = FastAPI(
    title="Choose Your Own Adventure Game API",
    description="An API for the Choose Your Own Adventure Game to generate story paths and manage game state.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)