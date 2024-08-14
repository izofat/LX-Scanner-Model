from pathlib import Path
from typing import List, Tuple, Union

from pydantic import BaseModel


class OCROutput(BaseModel):
    """
    This is the output of the OCR model
    """

    confidence: List[Union[float, int]]
    image_size: Tuple[int, int]
    image: Union[str, Path]
    text: List[str]
    locations: List[List[List[Union[int, float]]]]

    class Config:  # pylint: disable=too-few-public-methods
        """Added for numpy array"""

        arbitrary_types_allowed = True


class MarkerLines(BaseModel):
    """
    This is the model for the lines that are marked on the image
    """

    top_left: List[int]
    bottom_right: List[int]
    text: str
