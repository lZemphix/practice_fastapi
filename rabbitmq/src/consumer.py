import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import json

print("12312")
from pika import BlockingConnection

from src.producer import Produсer
from config.config import settings
from utils.telenotify import Telenotify


class Consumer:
    def __init__(self):
        pass

    def notify(self, ch, method, props, body: bytes):
        body = json.loads(body.decode())
        telenotify = Telenotify()
        message = f"""```\nID: {body['id']}\nTable: {body['table']}\nAction: {body['action']}\nData:\n\t{body['data']}```"""
        telenotify.send_message(message=message, title="Update!")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def create_queue(self):
        try:
            producer = Produсer(
                queue=settings.rabbitmq_queue_name,
                exchange=settings.rabbitmq_exchange_name,
                rk=settings.rabbitmq_rk,
            )
            return producer.create_queue()
        except:
            return 1

    def start_consuming(self):
        with BlockingConnection(settings.rabbitmq_params) as conn:
            with conn.channel() as ch:
                ch.basic_consume(
                    queue=settings.rabbitmq_queue_name, on_message_callback=self.notify
                )
                ch.start_consuming()


if __name__ == "__main__":
    consumer = Consumer()
    consumer.create_queue()
    consumer.start_consuming()
