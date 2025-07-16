from json import JSONDecodeError
from typing import Annotated, Any, Literal

import httpx
import typer

from src.cli.console import console, display_table, with_spinner
from src.core import get_app_config, get_resource_config

app_config = get_app_config()
resource_config = get_resource_config()

app = typer.Typer()


def _get_items(url: str, page: int, search: str | None, sort_by: str | None, order: str | None) -> list[dict[str, Any]]:
    """
    Fetches a list of items from the given url. If no items are found or an error occurs, returns an empty list.

    Args:
        page: Page number to fetch. Each page returns a fixed number of people.
        search: Optional search query to filter people by name (case-insensitive).
        sort_by: Optional field to sort the retrieved.
        order: Optional item order 'asc' or 'desc'. Defaults to 'asc'.
    """
    params: dict[str, Any] = {"page": page}
    if search:
        params["search"] = search
    if sort_by:
        params["sort_by"] = sort_by

    items: list[dict[str, Any]] = []

    try:
        response: httpx.Response = httpx.get(url=url, params=params)
        items.extend(response.json())
    except httpx.RequestError as e:
        console.print(f"[bold red]Error requesting data from {url=}:[/bold red] {repr(e)}")
    except httpx.HTTPStatusError as e:
        console.print(
            f"[bold red]Invalid response from {url=} with status_code={e.response.status_code}:[/bold red] {repr(e)}"
        )
    except JSONDecodeError as e:
        console.print(f"[bold red]Error decoding JSON from response:[/bold red] {repr(e)}")

    # If sort_by, backend returns items in asc order by default
    # Base on requirements, order must be set in CLI app, not backend
    if items and sort_by and order == "desc":
        items.reverse()

    return items


@app.command()
@with_spinner
def list_people(
    page: Annotated[int, typer.Option(help="Page number. Each page returns 10 items.")] = 1,
    search: Annotated[str | None, typer.Option(help="Partial name to filter results by. Case-insensitive.")] = None,
    sort_by: Annotated[str | None, typer.Option(help="Sort the results by the given field.")] = None,
    order: Annotated[
        Literal["asc", "desc"] | None,
        typer.Option(help="Items order if sort_by: 'asc' for ascending, 'desc' for descending. Defaults to 'asc'"),
    ] = None,
) -> None:
    """CLI command that fetches people from the SWAPI API and displays the result as a table."""
    items: list[dict[str, Any]] = _get_items(
        url=f"{app_config.url}/{resource_config.people_resource}/",
        page=page,
        search=search,
        sort_by=sort_by,
        order=order,
    )
    display_table(items=items)


@app.command()
@with_spinner
def list_planets(
    page: Annotated[int, typer.Option(help="Page number. Each page returns 10 items.")] = 1,
    search: Annotated[str | None, typer.Option(help="Partial name to filter results by. Case-insensitive.")] = None,
    sort_by: Annotated[str | None, typer.Option(help="Sort the results by the given field.")] = None,
    order: Annotated[
        Literal["asc", "desc"] | None,
        typer.Option(help="Items order if sort_by: 'asc' for ascending, 'desc' for descending. Defaults to 'asc'"),
    ] = None,
) -> None:
    """CLI command that fetches planets from the SWAPI API and displays the result as a table."""
    items: list[dict[str, Any]] = _get_items(
        url=f"{app_config.url}/{resource_config.planets_resource}/",
        page=page,
        search=search,
        sort_by=sort_by,
        order=order,
    )
    display_table(items=items)


if __name__ == "__main__":
    app()
