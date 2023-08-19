import unittest
import pathlib
import dataclasses
from recipe_scrapers import scrape_html

from extruct.jsonld import json

__file_dir = pathlib.Path(__file__).parent.absolute()


class RecipeTestCase(unittest.TestCase):
    def _test_recipe(self):
        pass


@dataclasses.dataclass(slots=True)
class TestCase:
    description: str
    expect: pathlib.Path | None
    html: pathlib.Path | None


@dataclasses.dataclass(slots=True)
class TestExpectations:
    yield_: str
    ingredients: list[str]
    title: str
    author: str
    host: str
    canonical_url: str
    image: str
    total_time: int
    instructions: str

    @classmethod
    def from_json(cls, file_path: pathlib.Path):
        with open(file_path, "r") as json_file:
            data = json.load(json_file)

        return cls(
            yield_=data.get("yield", ""),
            ingredients=data.get("ingredients", []),
            title=data.get("title", ""),
            author=data.get("author", ""),
            host=data.get("host", ""),
            canonical_url=data.get("canonical_url", ""),
            image=data.get("image", ""),
            total_time=data.get("total_time", 0),
            instructions=data.get("instructions", ""),
        )


def test_func_factory(test_case: TestCase):
    if not test_case.html or not test_case.expect:
        raise ValueError("TestCase must have html and expect set")

    def test_func(self):
        expect = TestExpectations.from_json(test_case.expect)
        got = scrape_html(test_case.html.read_text(), expect.canonical_url)

        self.assertEqual(expect.yield_, got.yields())
        self.assertEqual(expect.ingredients, got.ingredients())
        self.assertEqual(expect.title, got.title())
        self.assertEqual(expect.author, got.author())
        self.assertEqual(expect.host, got.host())
        self.assertEqual(expect.canonical_url, got.canonical_url())
        self.assertEqual(expect.image, got.image())
        self.assertEqual(expect.total_time, got.total_time())
        self.assertEqual(expect.instructions, got.instructions())

    return test_func


def load_test_cases():
    test_data = __file_dir / "testdata"

    for domain in test_data.iterdir():
        if not domain.is_dir():
            continue

        matches = {}

        for file in domain.iterdir():
            if not file.is_file():
                continue

            got = matches.get(file.stem, None)

            if got is None:
                got = TestCase(description=file.stem, expect=None, html=None)
                matches[file.stem] = got

            if file.suffix == ".json":
                got.expect = file
            elif file.suffix == ".html":
                got.html = file

            if got.html and got.expect:
                setattr(
                    RecipeTestCase,
                    f"test_{domain.stem}_{file.stem}",
                    test_func_factory(got),
                )

                del matches[file.stem]


if __name__ == "__main__":
    load_test_cases()
    unittest.main()
