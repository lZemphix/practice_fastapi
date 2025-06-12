from pydantic_settings import BaseSettings
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    db_url: str = getenv("DATABASE_URL")
    telegram_bot_id: str = getenv("TELEGRAM_BOT_ID")
    telegram_user_id: int = getenv("TELEGRAM_USER_ID")



settings = Settings()
