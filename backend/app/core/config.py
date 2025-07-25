"""Configuration settings for the application."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuration settings for the application.
    This class uses Pydantic to manage application settings, including database
    connection details and environment variables.
    """
    model_config = SettingsConfigDict(env_file='.env',env_file_encoding='utf-8', extra='ignore')

    DB_URL: str = ""
    USER: str, PASSWORD: str, DB_HOST: str, DB_PORT: int
    POWER_DB_NAME: str

    GROQ_API_KEY: str
    GROQ_MODEL: str

    JWT_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.DB_URL = (f"postgresql://{self.USER}:{self.PASSWORD}@"
                       f"{self.DB_HOST}:{self.DB_PORT}/{self.POWER_DB_NAME}"
        )

settings = Settings()
