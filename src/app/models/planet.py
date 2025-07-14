import pydantic

from src.app.models.base_model import WithTimestamps, WithUrl, model_field


class Planet(WithTimestamps, WithUrl):
    """Describes a Planet entity."""

    name: str
    rotation_period: str
    orbital_period: str
    diameter: str
    climate: str
    gravity: str
    terrain: str
    surface_water: str
    population: str
    residents: list[pydantic.HttpUrl] = model_field(default_factory=list)
    films: list[pydantic.HttpUrl] = model_field(default_factory=list)
