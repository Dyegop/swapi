import pydantic

from src.app.models.base_model import model_field


class Insight(pydantic.BaseModel):
    """Describes a generated AI insight entity."""

    name: str = model_field(
        title="Name",
        description="The name of the item we generates AI description from.",
    )

    description: str = model_field(
        title="Description",
        description="The generated AI description.",
    )
