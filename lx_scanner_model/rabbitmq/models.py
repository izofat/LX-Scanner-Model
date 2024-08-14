import datetime
import json
from pathlib import Path
from typing import List, Tuple, Union

from pydantic import BaseModel, Field


class RabbitMQInput(BaseModel):
    image: Union[str, Path]
    lang_list: List[str]


class RabbitMQOutput(BaseModel):
    text: List[str]
    confidence: List[Union[float, int]]
    image_size: Tuple[int, int]
    image: Union[str, Path]
    date: datetime.datetime = Field(default_factory=datetime.datetime.now)

    def to_json(self):
        output = self.model_dump()
        output["date"] = output["date"].strftime("%Y-%m-%d %H:%M:%S")
        return json.dumps(output).encode()
