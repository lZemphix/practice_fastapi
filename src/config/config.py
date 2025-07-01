from pydantic_settings import BaseSettings
from os import getenv
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    DB_USER: str = getenv("DATABASE_USER")
    DB_PASSWORD: str = getenv("DATABASE_PASSWORD")
    DB_HOST: str = getenv("DATABASE_HOST")
    DB_NAME: str = getenv("DATABASE_NAME")

    ADMIN_USERNAME: str = getenv("ADMIN_USERNAME")
    ADMIN_PASSWORD: str = getenv("ADMIN_PASSWORD")
    ADMIN_SECRETKEY: str = getenv("ADMIN_SECRETKEY")

    @property
    def db_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:5432/{self.DB_NAME}"


settings = Settings()
