import os
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    JWT_SECRET_KEY: str = Field(..., env="JWT_SECRET_KEY")
    JWT_ALGORITHM: str = Field(default="HS256", env="JWT_ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(
        default=60 * 24, env="ACCESS_TOKEN_EXPIRE_MINUTES"
    )
    PROJECT_NAME: str = "DevNotes"

    class Config:
        env_file = ".env"


settings = Settings()
