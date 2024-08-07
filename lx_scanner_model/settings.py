from typing import Optional

import toml
from pydash import get

config = toml.load("../config.toml")

DEBUG = get(config, "debug", True)


class RabbitMQConfig:
    _DEFAULT_HOST = "localhost"
    _DEFAULT_PORT = 5672
    _DEFAULT_USERNAME = "guest"
    _DEFAULT_PASSWORD = "guest"
    _DEFAULT_QUEUE_NAME = "queue"

    def __init__(self, queue_name: Optional[str] = None):
        if DEBUG:
            self.HOST = get(config, "rabbitmq.dev.host", self._DEFAULT_HOST)
            self.PORT = get(config, "rabbitmq.dev.port", self._DEFAULT_PORT)
            self.USERNAME = get(config, "rabbitmq.dev.username", self._DEFAULT_USERNAME)
            self.PASSWORD = get(config, "rabbitmq.dev.password", self._DEFAULT_PASSWORD)
        else:
            self.HOST = get(config, "rabbitmq.prod.host", self._DEFAULT_HOST)
            self.PORT = get(config, "rabbitmq.prod.port", self._DEFAULT_PORT)
            self.USERNAME = get(
                config, "rabbitmq.prod.username", self._DEFAULT_USERNAME
            )
            self.PASSWORD = get(
                config, "rabbitmq.prod.password", self._DEFAULT_PASSWORD
            )

        if queue_name:
            self.QUEUE_NAME = queue_name
        else:
            self.QUEUE_NAME = self._DEFAULT_QUEUE_NAME
