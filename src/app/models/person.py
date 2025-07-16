import pydantic

from src.app.models.base_model import WithTimestamps, WithUrl, model_field


class Person(WithUrl, WithTimestamps):
    """Describes a Person entity."""

    name: str = model_field(
        title="Name",
        description="The name of the person.",
    )

    height: str = model_field(
        title="Height",
        description="The height of the person in cm.",
    )

    mass: str = model_field(
        title="Mass",
        description="The mass of the person in kg.",
    )

    hair_color: str = model_field(
        title="Hair Color",
        description="The hair color of the person.",
    )

    skin_color: str = model_field(
        title="Skin Color",
        description="The skin color of the person.",
    )

    eye_color: str = model_field(
        title="Eye Color",
        description="The eye color of the person.",
    )

    birth_year: str = model_field(
        title="Birth Year",
        description="The birth year of the person.",
    )

    gender: str = model_field(
        title="Gender",
        description="The gender of the person.",
    )

    homeworld: pydantic.HttpUrl = model_field(
        title="Homeworld",
        description="URL of the person's home planet.",
    )

    films: list[pydantic.HttpUrl] = model_field(
        title="Films",
        description="A list of URLs to films this person appears in.",
        default_factory=list,
    )

    species: list[pydantic.HttpUrl] = model_field(
        title="Species",
        description="A list of URLs to species the person belongs to.",
        default_factory=list,
    )

    vehicles: list[pydantic.HttpUrl] = model_field(
        title="Vehicles",
        description="A list of URLs to vehicles the person has used.",
        default_factory=list,
    )

    starships: list[pydantic.HttpUrl] = model_field(
        title="Starships",
        description="A list of URLs to starships the person has piloted.",
        default_factory=list,
    )
