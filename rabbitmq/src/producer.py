import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pika import BlockingConnection
from config.config import settings


class Produсer:

    def __init__(self, queue: str, exchange: str, rk: str):
        self.queue = queue
        self.exchange = exchange
        self.rk = rk

    def create_queue(self) -> int:
        try:
            with BlockingConnection(settings.rabbitmq_params) as conn:
                with conn.channel() as ch:
                    ch.queue_declare(queue=self.queue, durable=True)

                    ch.queue_bind(
                        exchange=self.exchange, queue=self.queue, routing_key=self.rk
                    )
                    return 0
        except:
            return 1
