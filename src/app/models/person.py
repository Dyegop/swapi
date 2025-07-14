import pydantic

from src.app.models.base_model import WithTimestamps, WithUrl, model_field


class Person(WithUrl, WithTimestamps):
    """Describes a Person entity."""

    name: str
    height: str
    mass: str
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str
    homeworld: pydantic.HttpUrl
    films: list[pydantic.HttpUrl] = model_field(default_factory=list)
    species: list[pydantic.HttpUrl] = model_field(default_factory=list)
    vehicles: list[pydantic.HttpUrl] = model_field(default_factory=list)
    starships: list[pydantic.HttpUrl] = model_field(default_factory=list)
