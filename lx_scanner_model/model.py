from pathlib import Path
from typing import List, Union

from pydantic import BaseModel

# TODO keep adding fields


class OCROutput(BaseModel):
    confidence: List[Union[float, int]]
    image_size: int
    image: Union[Path, str]
    text: List[str]
    locations: List[List[List[Union[int, float]]]]


class MarkerLines(BaseModel):
    top_left: List[int]
    bottom_right: List[int]
    text: str


class FinalData(BaseModel):
    ocr_output: OCROutput
