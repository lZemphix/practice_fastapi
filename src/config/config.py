from pydantic_settings import BaseSettings
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    db_url: str = getenv("DATABASE_URL")


settings = Settings()
