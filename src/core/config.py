from functools import lru_cache

import pydantic
import pydantic_settings


class BaseConfig(pydantic_settings.BaseSettings):
    """Describes app configuration."""

    app_name: str = "swapi"
    app_host: str = "https://127.0.0.1"
    app_port: int = 8000
    reload: bool = False


class ResourceConfig(pydantic_settings.BaseSettings):
    """Describes SWAPI resource configuration."""

    base_url: pydantic.HttpUrl = "https://swapi.info/api"
    people_url: pydantic.HttpUrl = "https://swapi.info/api/people"
    planets_url: pydantic.HttpUrl = "https://swapi.info/api/planets"

    default_page_size: int = 10
    """Default items to return by page."""


@lru_cache()
def get_config() -> BaseConfig:
    """Returns an instance of BaseConfig."""
    return BaseConfig()


@lru_cache()
def get_resource_config() -> ResourceConfig:
    """Returns an instance of ResourceConfig."""
    return ResourceConfig()
