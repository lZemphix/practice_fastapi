import requests
from config.config import settings


class Telenotify:
    def __init__(self) -> None:
        self.BOT_TOKEN = settings.telegram_bot_id
        self.USER_ID = settings.telegram_user_id

    def send_message(self, message: str, title: str = "") -> int:
        msg = f"*{title}*\n{message}"
        url = f"https://api.telegram.org/bot{self.BOT_TOKEN}/sendMessage"
        payload = {"chat_id": self.USER_ID, "text": msg, "parse_mode": "Markdown"}

        resp = requests.post(url, json=payload)
        return resp.status_code
