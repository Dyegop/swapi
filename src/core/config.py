from functools import lru_cache
from urllib.parse import urljoin

import pydantic_settings


class AppConfig(pydantic_settings.BaseSettings):
    """Describes app configuration."""

    name: str = "swapi"
    host: str = "127.0.0.1"
    port: int = 8000
    reload: bool = False

    @property
    def url(self) -> str:
        return f"http://{self.host}:{self.port}"


class ResourceConfig(pydantic_settings.BaseSettings):
    """Describes SWAPI resource configuration."""

    people_resource: str = "people"
    planets_resource: str = "planets"
    base_url: str = "https://swapi.info/api/"
    people_endpoint: str = urljoin(base_url, people_resource)
    planets_endpoint: str = urljoin(base_url, planets_resource)

    default_page_size: int = 10
    """Default items to return by page."""


@lru_cache()
def get_app_config() -> AppConfig:
    """Returns a cached instance of the app configuration."""
    return AppConfig()


@lru_cache()
def get_resource_config() -> ResourceConfig:
    """Returns a cached instance of the resource configuration."""
    return ResourceConfig()
