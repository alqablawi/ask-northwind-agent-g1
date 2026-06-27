from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "Ask Northwind Agent"
    app_env: str = "local"
    debug: bool = True

@lru_cache
def get_settings() -> Settings:
    return Settings()