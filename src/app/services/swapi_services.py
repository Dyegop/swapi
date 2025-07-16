import asyncio
import re
from typing import Coroutine, Type, TypeVar

import httpx
import pydantic

from src.app.models import Person, Planet
from src.core import get_app_config, get_logger, get_resource_config

SwapiModel = TypeVar("SwapiModel", Person, Planet)

app_config = get_app_config()
resource_config = get_resource_config()

logger = get_logger(app_config.name)


async def _get_item(model: Type[SwapiModel], client: httpx.AsyncClient, endpoint: str) -> SwapiModel | None:
    """Retrieves an item from the specific endpoint and parse the result to the given model."""
    try:
        response: httpx.Response = await client.get(endpoint)
        if response.is_success:
            return model(**response.json())
        else:
            logger.error(f"Error retrieving item from {endpoint=} with status_code={response.status_code}.")
    except httpx.RequestError as e:
        logger.error(f"Unexpected error ocurred when executing request: {repr(e)}.")
    except pydantic.ValidationError as e:
        logger.error(f"Failed to parse response into {model.__name__} due to error: {repr(e)}.")
    return None


def _filter_by_name(items: list[SwapiModel], name: str) -> list[SwapiModel]:
    """Filter a list of items by the given case-insensitive name field."""
    pattern = re.compile(re.escape(name), re.IGNORECASE)
    return [item for item in items if pattern.search(item.name)]


async def list_items(
    model: Type[SwapiModel],
    *,
    url: str,
    page: int,
    search: str | None = None,
    sort_by: str | None = None,
) -> list[SwapiModel]:
    """
    Retrieves a list of SWAPI resources.

    Args:
        model: The Pydantic model to seralize retrieved resources.
        url: The URL of the SWAPI resource.
        page: The page number to fetch. Each page includes DEFAULT_PAGE_SIZE items.
        search: Substring to filter items by their `name` field. Case-insensitive.
        sort_by: Sort items by the given field.
    """

    start_id = (page - 1) * resource_config.default_page_size + 1
    end_id = start_id + resource_config.default_page_size

    async with httpx.AsyncClient() as client:
        tasks: list[Coroutine] = []

        for item_id in range(start_id, end_id):
            endpoint = f"{url}/{item_id}"
            tasks.append(_get_item(model=model, client=client, endpoint=endpoint))

        items: list[SwapiModel] = await asyncio.gather(*tasks)

    items = [item for item in items if item is not None]
    if search:
        items: list[SwapiModel] = _filter_by_name(items=items, name=search)
    if sort_by:
        items: list[SwapiModel] = sorted(items, key=lambda item: getattr(item, sort_by))

    return items
