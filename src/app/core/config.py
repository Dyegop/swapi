from functools import lru_cache

import pydantic
import pydantic_settings


class ResourceConfig(pydantic_settings.BaseSettings):
    """Describes SWAPI resource configuration."""

    swapi_url: pydantic.HttpUrl = "https://swapi.info/api"
    swapi_people_url: pydantic.HttpUrl = "https://swapi.info/api/people"
    swapi_planets_url: pydantic.HttpUrl = "https://swapi.info/api/planets"


@lru_cache()
def get_resource_config() -> ResourceConfig:
    """Returns an instance of ResourceConfig."""
    return ResourceConfig()
