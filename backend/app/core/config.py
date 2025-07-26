"""Configuration settings for the application."""
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field


class Settings(BaseSettings):
    """Configuration settings for the application using Pydantic.
    """
    model_config = SettingsConfigDict(
        env_file='.env',env_file_encoding='utf-8', extra='ignore')

    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    GROQ_API_KEY: str
    GROQ_MODEL: str

    """JWT settings
    JWT_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int"""
    
    @computed_field
    @property
    def DB_URL(self) -> str:
        return (f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@"
                f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

settings = Settings()
