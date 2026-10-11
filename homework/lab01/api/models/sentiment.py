from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class PredictRequest(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
    )

    text: str = Field(min_length=1, strict=True)


class PredictResponse(BaseModel):
    prediction: Literal["negative", "neutral", "positive"]
