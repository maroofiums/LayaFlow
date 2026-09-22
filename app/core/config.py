from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "LayaFlow"
    debug: bool = True
    laya_model: str = "convaiinnovations/laya"

settings = Settings()