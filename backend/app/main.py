from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.endpoints import user_queries, users

app = FastAPI(
    title="Pawa-bot API",
    description="API for the Pawa-bot application.",
    version="1.0.0",
)

# CORS configuration
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # Allows cookies to be included in cross-origin requests
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routers
app.include_router(users.router, prefix="/api/v1", tags=["Users"])
app.include_router(
    user_queries.router, prefix="/api/v1", tags=["User Queries"]
)