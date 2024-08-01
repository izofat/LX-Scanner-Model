from pathlib import Path
from typing import Union

import easyocr

from ..displayers.marker import Marker
from ..model import OCROutput


class OpticalCharacterRecognition(easyocr.Reader):
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
        self._output = None

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
        return self._output

    def read_text(self):
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
            return None

        self._locations = []
        self._words = []
        self._confidence_of_words = []

        for line in self.result:
            self._locations.append(line[0])
            self._words.append(line[1])
            self._confidence_of_words.append(line[2])

        self._output = OCROutput(
            confidence=self._confidence_of_words,
            image_size=0,  # TODO: Add image size
            image=self.image,
            text=self._words,
            locations=self._locations,
        )

    def display_text_locations(self):
        marker = Marker(self.image, self.locations, self._words)
        marker.display()
