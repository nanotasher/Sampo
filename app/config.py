import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Sampo"
    environment: str = os.getenv("ENVIRONMENT", "local")
    port: int = int(os.getenv("PORT", "8080"))

    db_url: str = os.getenv("DB_URL", "sqlite:///./sampo.db")

    alpaca_api_key: str | None = None
    alpaca_api_secret: str | None = None
    alpaca_env: str = "paper"  # paper/live later

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
