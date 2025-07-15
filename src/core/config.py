from functools import lru_cache

import pydantic
import pydantic_settings


class AppConfig(pydantic_settings.BaseSettings):
    """Describes app configuration."""

    app_name: str = "swapi"
    app_host: str = "127.0.0.1"
    app_port: int = 8000
    reload: bool = False


class ResourceConfig(pydantic_settings.BaseSettings):
    """Describes SWAPI resource configuration."""

    base_url: pydantic.HttpUrl = "https://swapi.info/api"
    people_url: pydantic.HttpUrl = "https://swapi.info/api/people"
    planets_url: pydantic.HttpUrl = "https://swapi.info/api/planets"

    default_page_size: int = 10
    """Default items to return by page."""


class CLIConfig(pydantic_settings.BaseSettings):
    """Describes SWAPI CLI configuration."""

    people_table_title: str = "People"
    planets_table_title: str = "Planets"


@lru_cache()
def get_app_config() -> AppConfig:
    """Returns a cached instance of the app configuration."""
    return AppConfig()


@lru_cache()
def get_resource_config() -> ResourceConfig:
    """Returns a cached instance of the resource configuration."""
    return ResourceConfig()


@lru_cache()
def get_cli_config() -> CLIConfig:
    """Returns a cached instance of the CLI app configuration."""
    return CLIConfig()
