from fastapi import FastAPI
from datetime import datetime, timezone
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173"
]

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