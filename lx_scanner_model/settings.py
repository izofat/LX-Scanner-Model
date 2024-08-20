from typing import Optional

import toml
from pydash import get

config = toml.load("./config.toml")

DEBUG = get(config, "debug", True)

OUTPUT_DIR = get(config, "output_file_path", "/srv/LX-Scanner/output")

INPUT_QUEUE = get(config, "rabbitmq.input_queue", "model-input")
OUTPUT_QUEUE = get(config, "rabbitmq.output_queue", "model-output")


class RabbitMQConfig:  # pylint: disable=too-few-public-methods
    _DEFAULT_HOST = "localhost"
    _DEFAULT_PORT = 5672
    _DEFAULT_USERNAME = "guest"
    _DEFAULT_PASSWORD = "guest"
    _DEFAULT_QUEUE_NAME = "queue"

    def __init__(self, queue_name: Optional[str] = None):
        env = "dev" if DEBUG else "prod"
        self.HOST = config.get(f"rabbitmq.{env}.host", self._DEFAULT_HOST)
        self.PORT = config.get(f"rabbitmq.{env}.port", self._DEFAULT_PORT)
        self.USERNAME = config.get(f"rabbitmq.{env}.username", self._DEFAULT_USERNAME)
        self.PASSWORD = config.get(f"rabbitmq.{env}.password", self._DEFAULT_PASSWORD)
        self.QUEUE_NAME = queue_name or self._DEFAULT_QUEUE_NAME
