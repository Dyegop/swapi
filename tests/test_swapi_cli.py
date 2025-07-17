import typer
from typer.testing import CliRunner

app = typer.Typer()
runner = CliRunner()


@app.command()
def list_people(page: int = 1, search: str = None, sort_by: str = None, order: str = None) -> None:
    print(f"Executing command with args {page=}, {search=}, {sort_by=}, {order=}.")


@app.command()
def list_planets(page: int = 1, search: str = None, sort_by: str = None, order: str = None) -> None:
    print(f"Executing command with args {page=}, {search=}, {sort_by=}, {order=}.")


class TestSwapiCLI:
    def test_list_people_with_args(self):
        result = runner.invoke(
            app, ["list-people", "--page", "2", "--search", "luke", "--sort-by", "name", "--order", "desc"]
        )
        assert result.exit_code == 0
        assert "luke" in result.output

    def test_list_planets_with_args(self):
        result = runner.invoke(app, ["list-planets", "--page", "10", "--search", "Earth", "--order", "desc"])
        assert result.exit_code == 0
        assert "Earth" in result.output

    def test_list_people_default_args(self):
        result = runner.invoke(app, ["list-people"])
        assert result.exit_code == 0

    def test_list_planets_default_args(self):
        result = runner.invoke(app, ["list-planets"])
        assert result.exit_code == 0
