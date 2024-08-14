from pathlib import Path
from typing import List, Optional, Union

import cv2
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from lx_scanner_model.scanner_model.model import MarkerLines
from lx_scanner_model.settings import DEBUG, OUTPUT_DIR


class Marker:  # pylint: disable=too-few-public-methods
    def __init__(self, image: Union[str, Path], locations, text):
        self.image = image
        self.locations = locations
        self.text = text
        self.marked_image: Optional[Union[str, Path]] = None

        self.start_marking()

    def start_marking(self):
        """
        This is the main function that displays the image with the marked locations
        """
        lines = self.__split_locations(self.locations, self.text)
        loaded_image = cv2.imread(self.image)
        self.__mark_image(lines, loaded_image)

    @staticmethod
    def __split_locations(locations, text) -> Optional[List[MarkerLines]]:
        """
        Splits the locations into individual words
        """
        if not locations or not text:
            return None

        lines: List[MarkerLines] = []
        for i, line in enumerate(locations):
            lines.append(
                MarkerLines(
                    top_left=[int(line[0][0]), int(line[0][1])],
                    bottom_right=[int(line[2][0]), int(line[2][1])],
                    text=text[i],
                )
            )

        return lines

    def __mark_image(self, lines: List[MarkerLines], image):
        """
        Marks the image with the lines
        """
        if not lines:
            return

        for line in lines:
            cv2.rectangle(image, line.top_left, line.bottom_right, (0, 255, 0), 2)

        fig = Figure(figsize=(10, 10))
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        ax.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        ax.axis("off")
        canvas.draw()

        if DEBUG:
            output_file = f"{OUTPUT_DIR}/test.jpg"
        else:
            output_file = ...  # type: ignore
            # TODO instead of marked image get next id from db and save it as marked_image_{id}.jpg

        self.marked_image = output_file
        fig.savefig(output_file)
