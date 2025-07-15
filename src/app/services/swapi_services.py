import re
from typing import Final, Type, TypeVar

import httpx
import pydantic
from fastapi import HTTPException

from src.app.models import Person, Planet
from src.core.logger import get_logger

DEFAULT_PAGE_SIZE: Final[int] = 10
"""Default items to return by page."""

SwapiModel = TypeVar("SwapiModel", Person, Planet)

logger = get_logger(__name__)


def _filter_by_name(items: list[SwapiModel], name: str) -> list[SwapiModel]:
    """Filter a given list of type `Model` by the given case-insensitive name field."""
    pattern = re.compile(re.escape(name), re.IGNORECASE)
    return [item for item in items if pattern.search(item.name)]


async def list_items(
    model: Type[SwapiModel],
    *,
    base_url: pydantic.HttpUrl,
    page: int,
    search: str | None = None,
    sort_by: str | None = None,
) -> list[SwapiModel]:
    """
    Retrieves a list of SWAPI resources.

    Args:
        model: The Pydantic model to seralize retrieved resources.
        base_url: The base URL of the SWAPI resource.
        page: The page number to fetch. Each page includes DEFAULT_PAGE_SIZE items.
        search: Substring to filter items by their `name` field. Case-insensitive.
        sort_by: Sort items by the given field.

    Returns:
        list[SwapiModel]: A list of model instances representing the fetched and processed resources.

    Raises:
        HTTPException: If a request fails unexpectedly or the external service is unavailable.
    """

    items: list[SwapiModel] = []

    start_id = (page - 1) * DEFAULT_PAGE_SIZE + 1
    end_id = start_id + DEFAULT_PAGE_SIZE

    async with httpx.AsyncClient() as client:
        for item_id in range(start_id, end_id):
            endpoint = f"{base_url}/{item_id}"
            try:
                response: httpx.Response = await client.get(endpoint)
            except httpx.RequestError as e:
                err_msg = "Unexpected error ocurred when executing request"
                logger.error(f"{err_msg}: {repr(e)}")
                raise HTTPException(status_code=503, detail=err_msg) from e

            if response.is_success:
                items.append(model(**response.json()))
            else:
                logger.error(f"Error retrieving item from {endpoint=} - status_code={response.status_code}")

    if search:
        items: list[SwapiModel] = _filter_by_name(items=items, name=search)
        logger.info(f"Items filtered where the name includes `{search}`")

    if sort_by:
        items: list[SwapiModel] = sorted(items, key=lambda item: getattr(item, sort_by))
        logger.info(f"Items sorted by field `{sort_by}`")

    return items
