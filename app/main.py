from fastapi import FastAPI

from app.core.config import settings
from app.api.routes import router

app = FastAPI(
    title=settings.app_name,
    version="0.1.0"
)

app.include_router(router)


@app.get("/health")
def health_check():
    return {
        "status": "OK",
        "service": settings.app_name,
    }