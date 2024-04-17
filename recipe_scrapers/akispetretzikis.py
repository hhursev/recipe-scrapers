# mypy: disallow_untyped_defs=False
import json

from ._abstract import AbstractScraper


class AkisPetretzikis(AbstractScraper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.recipe_json = json.loads(
            self.soup.find("script", {"id": "__NEXT_DATA__"}).get_text()
        )

    @classmethod
    def host(cls):
        return "akispetretzikis.com"

    def category(self):
        return self.schema.category()

    def yields(self):
        return self.schema.yields()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()

    def language(self):
        return self.recipe_json["locale"]
