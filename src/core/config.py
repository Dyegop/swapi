from functools import lru_cache

import pydantic
import pydantic_settings


class BaseConfig(pydantic_settings.BaseSettings):
    """Describes app configuration."""


class ResourceConfig(pydantic_settings.BaseSettings):
    """Describes SWAPI resource configuration."""

    swapi_url: pydantic.HttpUrl = "https://swapi.info/api"
    swapi_people_url: pydantic.HttpUrl = "https://swapi.info/api/people"
    swapi_planets_url: pydantic.HttpUrl = "https://swapi.info/api/planets"


@lru_cache()
def get_config() -> BaseConfig:
    """Returns an instance of BaseConfig."""
    return BaseConfig()


@lru_cache()
def get_resource_config() -> ResourceConfig:
    """Returns an instance of ResourceConfig."""
    return ResourceConfig()
