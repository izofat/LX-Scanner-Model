from lx_scanner_model.rabbitmq.connection import RabbitMQConnection
from lx_scanner_model.rabbitmq.models import RabbitMQOutput
from lx_scanner_model.settings import RabbitMQConfig


class RabbitMQPublisher:
    """RabbitMQ publisher"""

    def __init__(self, queue_name: str):
        self.config = RabbitMQConfig(queue_name)
        self.connection = RabbitMQConnection(self.config)

    def connect(self):
        """connect to RabbitMQ server"""
        self.connection.connect()

    def publish_message(self, message: RabbitMQOutput):
        """publish message to RabbitMQ server"""
        self.connection.publish_message(message.to_json())

    def close(self):
        """close connection to RabbitMQ server"""
        self.connection.close()
