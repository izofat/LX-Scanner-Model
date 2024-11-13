import logging
import traceback


class Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(message)s")
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    @classmethod
    def info(cls, message, *args):
        cls.logger.info(message, *args)

    @classmethod
    def error(cls, exception: Exception):
        error_traceback = traceback.format_exc()
        cls.logger.error(
            "Exception occurred: %s\nTraceback: %s", str(exception), error_traceback
        )
