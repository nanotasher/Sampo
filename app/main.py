from fastapi import FastAPI
from .config import settings

app = FastAPI(title=settings.app_name)


@app.get("/health")
def health():
    return {"status": "ok", "environment": settings.environment}


@app.get("/")
def root():
    return {"message": "Sampo API is alive"}
