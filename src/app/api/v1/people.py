from enum import StrEnum
from typing import Annotated, Any

from fastapi import APIRouter, Query

from src.app.api.dependencies import list_items
from src.app.models import Person
from src.core import get_resource_config

router = APIRouter()


class PersonSortingField(StrEnum):
    """Describes fields that are allowed for sorting a Person entity."""

    NAME = "name"
    HEIGHT = "height"
    MASS = "mass"
    BIRTH_YEAR = "birth_year"
    CREATED = "created"
    EDITED = "edited"


@router.get("/people", response_model=list[Person], tags=["people"])
async def list_people(
    page: Annotated[int, Query(ge=1)] = 1,
    search: str | None = None,
    sort_by: PersonSortingField | None = None,
) -> Any:
    """
    Returns a paginated list of people from SWAPI.

    Args:
        page: Page number. Each page returns 10 items.
        search: Partial name to filter results by. Case-insensitive.
        sort_by: Sort the results by the given field.
    """

    resource_config = get_resource_config()

    people: list[Person] = await list_items(
        Person,
        base_url=resource_config.swapi_people_url,
        page=page,
        search=search,
        sort_by=sort_by,
    )

    return people
