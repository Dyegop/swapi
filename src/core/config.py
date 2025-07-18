from functools import lru_cache

import pydantic
import pydantic_settings

model_field = pydantic.Field


class BaseConfig(pydantic_settings.BaseSettings):
    """Base Config for all configurations."""

    model_config = pydantic_settings.SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="allow",
    )


class AppConfig(BaseConfig):
    """Describes app configuration."""

    name: str = model_field(
        title="Name",
        description="The name of the application.",
    )

    host: str = model_field(
        title="Host",
        description="The hostname or IP address where the app will run.",
    )

    port: int = model_field(
        title="Port",
        description="The port number the application will bind to.",
    )

    reload: bool = model_field(
        default=False,
        title="Reload",
        description="True for auto-reload, False otherwise.",
    )
    people_path: str = model_field(
        title="People Path",
        description="The path for the people endpoint.",
    )
    planets_path: str = model_field(
        title="Planets Path",
        description="The path for the planets endpoint.",
    )
    ai_insights_path: str = model_field(
        title="AI Path",
        description="The path for the AI insights endpoint.",
    )

    @property
    def url(self) -> str:
        return f"http://{self.host}:{self.port}"

    @property
    def people_url(self) -> str:
        return f"http://{self.host}:{self.port}{self.people_path}/"

    @property
    def planets_url(self) -> str:
        return f"http://{self.host}:{self.port}{self.planets_path}/"


class ResourceConfig(BaseConfig):
    """Describes resources configuration."""

    swapi_base_url: str = model_field(
        title="SWAPI Base URL",
        description="The base URL for the Star Wars API.",
    )

    people_endpoint: str = model_field(
        title="People Endpoint",
        description="The endpoint path for accessing people data.",
    )

    planets_endpoint: str = model_field(
        title="Planets Endpoint",
        description="The endpoint path for accessing planets data.",
    )

    default_page_size: int = model_field(
        ge=1,
        title="Default Page Size",
        description="The default number of items per page (minimum 1).",
    )


@lru_cache()
def get_app_config() -> AppConfig:
    """Returns a cached instance of the app configuration."""
    return AppConfig()


@lru_cache()
def get_resource_config() -> ResourceConfig:
    """Returns a cached instance of the resource configuration."""
    return ResourceConfig()
