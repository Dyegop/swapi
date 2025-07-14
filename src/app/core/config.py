import pydantic
import pydantic_settings


class Config(pydantic_settings.BaseSettings):
    """Describes app configuration."""

    swapi_base_url: pydantic.HttpUrl = "https://swapi.info/api"
    swapi_people_url: pydantic.HttpUrl = "https://swapi.info/api/people"
    swapi_planets_url: pydantic.HttpUrl = "https://swapi.info/api/planets"
