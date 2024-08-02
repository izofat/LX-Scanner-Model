from PIL import Image

from .marker import Marker


class ImageHelper:
    def __init__(self, marker: Marker):
        self.marker = marker

    @staticmethod
    def get_image_size(image_path):
        """
        Returns the size of the image
        """
        image = Image.open(image_path)
        return image.size

    def display_image(self):
        self.marker.display_image()

    @property
    def marked_image(self):
        return self.marker.marked_image
