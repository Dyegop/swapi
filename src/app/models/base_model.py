import datetime

import pydantic

model_field = pydantic.Field


class WithTimestamps(pydantic.BaseModel):
    """Describes a base model with timestamps."""

    created: datetime.datetime = model_field(title="Created", description="The resource creation datetime.")

    edited: datetime.datetime = model_field(
        title="Edited",
        description="The datetime when the resource was last modified.",
    )


class WithUrl(pydantic.BaseModel):
    """Describes a base model with resource url."""

    url: pydantic.HttpUrl = model_field(title="Url", description="The resource url.")
