from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = "Cat charity"
    description: str = "Cat charity app"
    database_url: str = "sqlite+aiosqlite:///./fastapi.db"
    secret: str = "SECRET"
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = ".env"


settings = Settings()
