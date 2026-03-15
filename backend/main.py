import os
from fastapi import FastAPI
from datetime import datetime, timezone
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

 # CORS 허용 IP 목록
origins = []

for origin in os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(","):
    if origin.strip():
        origins.append(origin.strip())

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {
        "status": "ok",
        "version": "0.0.1",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }