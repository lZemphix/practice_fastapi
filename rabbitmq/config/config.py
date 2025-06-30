from pika import ConnectionParameters
from pydantic_settings import BaseSettings
from os import getenv
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    telegram_bot_id: str = getenv("TELEGRAM_BOT_ID")
    telegram_user_id: str = getenv("TELEGRAM_USER_ID")

    rabbitmq_params: ConnectionParameters = ConnectionParameters(
        host="rabbitmq", port="5672"
    )
    rabbitmq_queue_name: str = getenv("RMQ_QUEUE_NAME")
    rabbitmq_exchange_name: str = getenv("RMQ_EXCHANGE_NAME")
    rabbitmq_rk: str = getenv("RMQ_RK")


settings = Settings()
