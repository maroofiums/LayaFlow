from fastapi import FastAPI

from app.api.routes import router
from app.core.config import settings
from app.database.database import Base, engine
from app.database import models


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
)

app.include_router(router)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": settings.app_name,
    }