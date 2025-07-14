import datetime
from typing import TypeVar

import pydantic

model_field = pydantic.Field

Model = TypeVar("Model", bound="BaseModel")
"""A Pydantic-based model."""


class WithTimestamps(pydantic.BaseModel):
    """Describes a base model with timestamps."""

    created: datetime.datetime
    edited: datetime.datetime


class WithUrl(pydantic.BaseModel):
    """Describes a base model with resource url."""

    url: pydantic.HttpUrl
