from pathlib import Path
from typing import Union

import easyocr  # type: ignore

from ..helpers.image import ImageHelper
from ..helpers.marker import Marker
from ..model import OCROutput


class OpticalCharacterRecognition(easyocr.Reader):
    image_helper: ImageHelper

    def __init__(self, image: Union[str, Path], lang_list="en", save_image=True):
        if isinstance(lang_list, str):
            lang_list = [lang_list]

        super().__init__(lang_list=lang_list, gpu=False)

        self.lang_list = lang_list
        self.image = image
        self.save_image = save_image
        self.result = None
        self._locations = None
        self._words = None
        self._confidence_of_words = None

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
        self._confidence_of_words = []

        for line in self.result:
            self._locations.append(line[0])
            self._words.append(line[1])
            self._confidence_of_words.append(line[2])

        self.image_helper = ImageHelper(Marker(self.image, self.locations, self._words))

    @property
    def locations(self):
        return self._locations

    @property
    def words(self):
        return self._words

    @property
    def confidence_of_words(self):
        return self._confidence_of_words

    @property
    def output(self) -> Union[OCROutput, None]:
        if not self._locations or not self._words or not self._confidence_of_words:
            return None

        return OCROutput(
            confidence=self._confidence_of_words,
            image_size=self.image_helper.get_image_size(self.image),
            image=self.image_helper.marked_image,
            text=self._words,
            locations=self._locations,
        )
