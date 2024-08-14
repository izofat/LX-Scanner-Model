from ..settings import RabbitMQConfig
from .connection import RabbitMQConnection


class RabbitMQConsumer:
    """RabbitMQ consumer"""

    def __init__(self, queue_name: str):
        self.config = RabbitMQConfig(queue_name)
        self.connection = RabbitMQConnection(self.config)

    def connect(self):
        self.connection.connect()

    def start_consuming(self, callback):
        """start consuming messages from RabbitMQ server"""
        self.connection.consume(callback)
