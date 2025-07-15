from enum import StrEnum
from typing import Annotated, Any

from fastapi import APIRouter, Query

from src.app.models import Person
from src.app.services import list_items
from src.core import get_resource_config

router = APIRouter()

resource_config = get_resource_config()


class PersonSortingField(StrEnum):
    """Describes fields that are allowed for sorting a Person entity."""

    NAME = "name"
    HEIGHT = "height"
    MASS = "mass"
    BIRTH_YEAR = "birth_year"
    CREATED = "created"
    EDITED = "edited"


@router.get("/", response_model=list[Person], tags=["people"])
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

    people: list[Person] = await list_items(
        Person,
        url=resource_config.people_url,
        page=page,
        search=search,
        sort_by=sort_by,
    )

    return people
