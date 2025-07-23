"""Configuration settings for the application."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuration settings for the application.
    This class uses Pydantic to manage application settings, including database
    connection details and environment variables.
    """
    model_config = SettingsConfigDict(env_file='.env',env_file_encoding='utf-8', extra='ignore')

    DB_URL: str = ""
    DB_USER: str, DB_PASSWORD: str, DB_HOST: str, DB_PORT: int
    DB_NAME: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.DB_URL = (f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@"
                       f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

settings = Settings()
