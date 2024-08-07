from typing import Optional

import pika

from ..settings import RabbitMQConfig


class RabbitMQConnection:
    """
    This class created for RabbitMQ connection
    You should create an instance of this class for every queue you want to connect
    """

    def __init__(self, config: RabbitMQConfig):
        self._host = config.HOST
        self._port = config.PORT
        self._creds = pika.PlainCredentials(config.USERNAME, config.PASSWORD)
        self._queue_name = config.QUEUE_NAME
        self._connection: Optional[pika.BlockingConnection] = None
        self._channel = None

    def connect(self):
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=self._host,
                port=self._port,
                credentials=self._creds,
            )
        )
        self._channel = self._connection.channel()

        self._channel.queue_declare(queue=self._queue_name)

        print(f"Connection {self._queue_name} established")

    def close(self):
        if self._connection.is_open:
            self._connection.close()
            print("RabbitMQ Connection Closed")

    def publish_message(self, message):
        self._channel.basic_publish(
            exchange="",
            routing_key=self._queue_name,
            body=message,
        )
        print(f"Message published to {self._queue_name}")

    def consume(self, callback):
        self._channel.basic_consume(
            queue=self._queue_name,
            on_message_callback=callback,
            auto_ack=True,
        )
        print(f"Consuming from {self._queue_name}")
        self._channel.start_consuming()
