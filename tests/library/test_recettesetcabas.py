import json
import pathlib
import unittest

from bs4 import BeautifulSoup

from recipe_scrapers import scrape_html


class RecettesEtCabasTest(unittest.TestCase):
    test_data = pathlib.Path(
        "tests/test_data/recettesetcabas.com/recettesetcabas_4.testhtml"
    )
    expected_data = pathlib.Path(
        "tests/test_data/recettesetcabas.com/recettesetcabas_4.json"
    )
    url = (
        "https://www.recettesetcabas.com/recettes/"
        "3992-ble-pilaf-chou-fleur-abricots-secs-orange"
    )

    def test_instructions_fall_back_to_unclassified_numbered_paragraphs(self):
        soup = BeautifulSoup(self.test_data.read_text(encoding="utf-8"), "html.parser")
        for script in soup.select('script[type="application/ld+json"]'):
            if not script.string:
                continue
            schema = json.loads(script.string)
            if schema.get("@type") == "Recipe":
                schema["recipeInstructions"] = []
                script.string = json.dumps(schema)
                break

        expected = json.loads(self.expected_data.read_text(encoding="utf-8"))
        scraper = scrape_html(str(soup), self.url)

        self.assertEqual(expected["instructions_list"], scraper.instructions_list())


if __name__ == "__main__":
    unittest.main()
