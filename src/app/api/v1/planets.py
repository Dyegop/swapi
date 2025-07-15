import asyncio
from enum import StrEnum
from typing import Annotated, Any

from fastapi import APIRouter, Query

from src.app.api.dependencies import list_items
from src.app.core import get_resource_config
from src.app.models import Planet

router = APIRouter()


class PlanetSortingField(StrEnum):
    """Describes fields that are allowed for sorting a Planet entity."""

    NAME = "name"
    ROTATION_PERIOD = "rotation_period"
    ORBITAL_PERIOD = "orbital_period"
    DIAMETER = "diameter"
    CLIMATE = "climate"
    GRAVITY = "gravity"
    POPULATION = "population"
    CREATED = "created"
    EDITED = "edited"


@router.get("/planets", response_model=list[Planet], tags=["people"])
async def list_planets(
    page: Annotated[int, Query(ge=1)] = 1,
    search: str | None = None,
    sort_by: PlanetSortingField | None = None,
) -> Any:
    """
    Returns a paginated list of planets from SWAPI.

    Args:
        page: Page number. Each page returns 10 items.
        search: Partial name to filter results by. Case-insensitive.
        sort_by: Sort the results by the given field.
    """

    resource_config = get_resource_config()

    planets: list[Planet] = await list_items(
        Planet,
        base_url=resource_config.swapi_planets_url,
        page=page,
        search=search,
        sort_by=sort_by,
    )

    return planets


async def main():
    result = await list_planets(page=40)
    print(result)


asyncio.run(main())
