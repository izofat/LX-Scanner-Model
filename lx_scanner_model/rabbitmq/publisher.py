from ..settings import RabbitMQConfig
from .connection import RabbitMQConnection


class RabbitMQPublisher:
    """RabbitMQ publisher"""

    def __init__(self, queue_name: str):
        self.config = RabbitMQConfig(queue_name)
        self.connection = RabbitMQConnection(self.config)

    def connect(self):
        """connect to RabbitMQ server"""
        self.connection.connect()

    def publish_message(self, message):
        """publish message to RabbitMQ server"""
        self.connection.publish_message(message)

    def close(self):
        """close connection to RabbitMQ server"""
        self.connection.close()
