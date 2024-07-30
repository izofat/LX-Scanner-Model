from pathlib import Path
from typing import Union

from pydantic import BaseModel

# TODO keep adding fields


class OCROutput(BaseModel):
    confidence: float
    image_size: int
    image: Union[bytes, Path]


class OCROutputSingleLine(OCROutput):
    text: str
    text_location: tuple[int, int, int, int]


class OCROutputMultipleLines(OCROutput):
    text: list[str]
    text_location: list[tuple[int, int, int, int]]


class FinalData(BaseModel):
    ocr_output: Union[OCROutputSingleLine, OCROutputMultipleLines]
