from pathlib import Path

import easyocr


class OpticalCharacterRecognition(easyocr.Reader):
    def __init__(self, image: Path, lang_list="en", save_image=True):
        if isinstance(lang_list, str):
            lang_list = [lang_list]

        self.lang_list = lang_list
        self.image = image
        self.save_image = save_image
        self.result = None
        super().__init__(lang_list=lang_list, gpu=False)

    def read_text(self, image_path: Path):
        self.result = self.readtext(image_path)
        # TODO parse result fill the model from the base
