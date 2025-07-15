import datetime

import pydantic

model_field = pydantic.Field


class WithTimestamps(pydantic.BaseModel):
    """Describes a base model with timestamps."""

    created: datetime.datetime
    edited: datetime.datetime


class WithUrl(pydantic.BaseModel):
    """Describes a base model with resource url."""

    url: pydantic.HttpUrl
