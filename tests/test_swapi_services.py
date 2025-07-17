import random
import re
from typing import Final

import pydantic
import pytest

DEFAULT_PAGE_SIZE: Final[int] = 10


class SomeSwapiModel(pydantic.BaseModel):
    name: str
    url: str
    sorting_field: int


class TestSwapiServices:
    @pytest.fixture
    def base_url(self) -> str:
        return "http://swapi.info/api/mock"

    @pytest.fixture
    def model_list(self, base_url: str) -> list[SomeSwapiModel]:
        return [SomeSwapiModel(name=f"Person{idx}", url=f"{base_url}/{idx}", sorting_field=idx) for idx in range(1, 31)]

    @pytest.mark.parametrize(
        "page, expected_urls",
        [
            (1, [f"http://swapi.info/api/mock/{idx}" for idx in range(1, 11)]),
            (2, [f"http://swapi.info/api/mock/{idx}" for idx in range(11, 21)]),
            (3, [f"http://swapi.info/api/mock/{idx}" for idx in range(21, 31)]),
        ],
    )
    def test_pagination(self, page: int, expected_urls: list[str], model_list: list[SomeSwapiModel]):
        start_id = (page - 1) * DEFAULT_PAGE_SIZE + 1
        end_id = start_id + DEFAULT_PAGE_SIZE

        retrieved_items: list[SomeSwapiModel] = []
        for item_id in range(start_id, end_id):
            retrieved_items.append(model_list[item_id - 1])

        assert len(retrieved_items) == DEFAULT_PAGE_SIZE

        retrieve_urls = [model.url for model in retrieved_items]
        assert retrieve_urls == expected_urls

    @pytest.mark.parametrize(
        "name, expected_names",
        [
            (
                "Person1",
                [
                    "Person1",
                    "Person10",
                    "Person11",
                    "Person12",
                    "Person13",
                    "Person14",
                    "Person15",
                    "Person16",
                    "Person17",
                    "Person18",
                    "Person19",
                ],
            ),
            ("Person21", ["Person21"]),
            ("Foo", []),
        ],
    )
    def test_search(self, name: str, expected_names: list[str], model_list: list[SomeSwapiModel]):
        pattern = re.compile(re.escape(name), re.IGNORECASE)
        result = [model.name for model in model_list if pattern.search(model.name)]

        assert result == expected_names

    def test_sorting(self, model_list: list[SomeSwapiModel]):
        random.shuffle(model_list)
        sorted_models: list[SomeSwapiModel] = sorted(model_list, key=lambda item: getattr(item, "sorting_field"))

        assert sorted_models[0].name == "Person1"
        assert sorted_models[-1].name == "Person30"
