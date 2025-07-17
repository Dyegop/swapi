from functools import lru_cache

import pydantic_settings


class AppConfig(pydantic_settings.BaseSettings):
    """Describes app configuration."""

    name: str = "swapi"
    host: str = "127.0.0.1"
    port: int = 8000
    reload: bool = False
    people_path: str = "/people"
    planets_path: str = "/planets"
    ai_insights_path: str = "/simulate_ai_insight"

    @property
    def url(self) -> str:
        return f"http://{self.host}:{self.port}"

    @property
    def people_url(self) -> str:
        return f"http://{self.host}:{self.port}{self.people_path}/"

    @property
    def planets_url(self) -> str:
        return f"http://{self.host}:{self.port}{self.planets_path}/"


class ResourceConfig(pydantic_settings.BaseSettings):
    """Describes resources configuration."""

    swapi_base_url: str = "https://swapi.info/api/"
    people_endpoint: str = f"{swapi_base_url}/people"
    planets_endpoint: str = f"{swapi_base_url}/planets"

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
