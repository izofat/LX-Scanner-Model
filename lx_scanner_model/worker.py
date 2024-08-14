import json
from typing import Optional

from pika.channel import Channel

from lx_scanner_model.ai_model.pretrained import OpticalCharacterRecognition
from lx_scanner_model.rabbitmq.consumer import RabbitMQConsumer
from lx_scanner_model.rabbitmq.models import RabbitMQInput, RabbitMQOutput
from lx_scanner_model.rabbitmq.publisher import RabbitMQPublisher
from lx_scanner_model.scanner_model.model import OCROutput
from lx_scanner_model.settings import INPUT_QUEUE, OUTPUT_QUEUE


class Worker:
    consumer = RabbitMQConsumer(INPUT_QUEUE)
    publisher = RabbitMQPublisher(OUTPUT_QUEUE)

    def launch(self):
        print("Worker is running")
        self.consumer.connect()
        self.consumer.start_consuming(self.callback)

    def callback(self, ch: Channel, method, _properties, body):
        model_input = json.loads(body)
        mq_input = RabbitMQInput(**model_input)

        self.process(mq_input.image, mq_input.lang_list, ch, method)

    def process(self, image, lang_list_image, ch: Channel, method):
        try:
            ocr = OpticalCharacterRecognition(image, lang_list_image)
            ocr.start_ocr()
            self.publish_output(ocr.output)
        except Exception as err:
            # TODO add custom exception handling
            ch.basic_ack(delivery_tag=method.delivery_tag)
            raise err

    def publish_output(self, output: Optional[OCROutput]):
        if not output:
            return

        mq_output = RabbitMQOutput(**output.model_dump())
        self.publisher.connect()
        self.publisher.publish_message(mq_output)
        self.publisher.close()

        print("Process completed")
