from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.core.config import config
from src.infrastructure.posts.router import router as posts_routes

app = FastAPI(
    version='0.1',
    root_path="/dev"
)


app.include_router(posts_routes)

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



