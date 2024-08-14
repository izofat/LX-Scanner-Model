from pathlib import Path
from typing import Union

import easyocr  # type: ignore

from lx_scanner_model.helpers.image import ImageHelper
from lx_scanner_model.helpers.marker import Marker
from lx_scanner_model.scanner_model.model import OCROutput


class OpticalCharacterRecognition(
    easyocr.Reader
):  # pylint: disable=too-many-instance-attributes
    image_helper: ImageHelper

    def __init__(self, image: Union[str, Path], lang_list="en"):
        if isinstance(lang_list, str):
            lang_list = [lang_list]

        super().__init__(lang_list=lang_list, gpu=False)

        self.lang_list = lang_list
        self.image = image
        self.result = None
        self._locations = None
        self._words = None
        self._confidence_of_lines = None

        self.start_ocr()

    def start_ocr(self):
        """
        Reads text from the pretrained ocr model

        Each tuple in result is a line

        result[0] ==> location of the line

        result[1] ==> words in the line

        result[2] ==> confidence of the model
        """
        self.result = self.readtext(self.image)
        self.__parse_result()

    def __parse_result(self):
        if not self.result:
            return

        self._locations = []
        self._words = []
        self._confidence_of_lines = []

        for line in self.result:
            self._locations.append(line[0])
            self._words.append(line[1])
            self._confidence_of_lines.append(line[2])

        self.image_helper = ImageHelper(
            Marker(self.image, self._locations, self._words)
        )

    @property
    def locations(self):
        return self._locations

    @property
    def words(self):
        return self._words

    @property
    def confidence_of_words(self):
        return self._confidence_of_lines

    @property
    def output(self) -> Union[OCROutput, None]:
        if not self._locations or not self._words or not self._confidence_of_lines:
            return None

        return OCROutput(
            confidence=self._confidence_of_lines,
            image_size=self.image_helper.get_image_size(self.image),
            image=self.image_helper.marked_image,
            text=self._words,
            locations=self._locations,
        )
