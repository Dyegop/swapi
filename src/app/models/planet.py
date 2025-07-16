import pydantic

from src.app.models.base_model import WithTimestamps, WithUrl, model_field


class Planet(WithTimestamps, WithUrl):
    """Describes a Planet entity."""

    name: str = model_field(
        title="Name",
        description="The name of the planet.",
    )

    rotation_period: str = model_field(
        title="Rotation Period",
        description="The rotation period of the planet in hours.",
    )

    orbital_period: str = model_field(
        title="Orbital Period",
        description="The orbital period of the planet in hours.",
    )

    diameter: str = model_field(
        title="Diameter",
        description="The diameter of the planet in km.",
    )

    climate: str = model_field(
        title="Climate",
        description="The climate type of the planet.",
    )

    gravity: str = model_field(
        title="Gravity",
        description="The gravity of the planet relative to Earth gravity.",
    )

    terrain: str = model_field(
        title="Terrain",
        description="The terrain features of the planet.",
    )

    surface_water: str = model_field(
        title="Surface Water",
        description="The percentage of the planet's surface that is covered in water.",
    )
    population: str = model_field(
        title="Population",
        description="The population of the planet.",
    )

    residents: list[pydantic.HttpUrl] = model_field(
        title="Residents",
        description="A list of URLs to people who reside on this planet.",
        default_factory=list,
    )
    films: list[pydantic.HttpUrl] = model_field(
        title="Films",
        description="A list of URLs to films in which this planet appears.",
        default_factory=list,
    )
