from pydantic_settings import BaseSettings
from functools import lru_cache
import os


class Settings(BaseSettings):
    """Configuración de la aplicación."""

    # Aplicación
    APP_NAME: str = "Gestion Profesoral API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # URL completa de PostgreSQL
    DB_POSTGRES: str

    @property
    def DATABASE_URL(self) -> str:
        return self.DB_POSTGRES

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Obtiene la configuración cacheada."""
    return Settings()