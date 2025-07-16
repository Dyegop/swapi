from functools import wraps
from typing import Any, Callable, ParamSpec, TypeVar

from rich.console import Console
from rich.table import Table

T = TypeVar("T")
P = ParamSpec("P")

console = Console()


def _format_table_value(value: Any) -> str:
    """Format value for display in a Rich table cell."""
    if value is None:
        return ""
    if isinstance(value, list):
        return "\n".join(str(v) for v in value)
    if isinstance(value, str):
        return value
    return str(value)


def with_spinner(f: Callable[P, T]) -> Callable[P, T]:
    """A simple decorator to add a spinner animation to a CLI command."""

    @wraps(f)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        with console.status("[bold green]Loading...[/bold green]"):
            return f(*args, **kwargs)

    return wrapper


def display_table(items: list[dict[str, Any]]) -> None:
    """Shows a pre-configured table with the given items."""

    if not items:
        console.print("[bold yellow]No results found.[/bold yellow]")
        return

    table = Table()

    # FastAPI app ensures all items have a similar schema, so we can grab column names from items[0]
    for item_keyname in items[0].keys():
        table.add_column(header=item_keyname.capitalize())

    for item in items:
        table.add_row(*[_format_table_value(v) for v in item.values()])

    console.print(table)
