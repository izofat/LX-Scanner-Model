from pathlib import Path
from typing import List, Tuple, Union

from pydantic import BaseModel


class OCROutput(BaseModel):
    """
    This is the output of the OCR model
    """

    confidence: List[Union[float, int]]
    image_size: Tuple[int, int]
    image: Union[Path, str]
    text: List[str]
    locations: List[List[List[Union[int, float]]]]


class MarkerLines(BaseModel):
    """
    This is the model for the lines that are marked on the image
    """

    top_left: List[int]
    bottom_right: List[int]
    text: str


# class FinalData(BaseModel):
#     ocr_output: OCROutput
