from typing import List, Optional

import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from lx_scanner_model.scanner_model.model import MarkerLines
from lx_scanner_model.settings import DEBUG


class Marker:
    def __init__(self, image, locations, text):
        self.image = image
        self.locations = locations
        self.text = text
        self.marked_image = None

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

        image_from_plot = np.frombuffer(canvas.tostring_rgb(), dtype="uint8")
        image_from_plot = image_from_plot.reshape(
            fig.canvas.get_width_height()[::-1] + (3,)
        )

        self.marked_image = image_from_plot

        if DEBUG:
            fig.savefig("../.secret/plot.png")

    def display_image(self):
        """
        Displays the marked image
        """

        plt.figure(figsize=(10, 10))
        plt.imshow(self.marked_image)
        plt.axis("off")
        plt.show()
