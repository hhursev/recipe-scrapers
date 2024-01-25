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

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()

    def language(self):
        return self.recipe_json["locale"]
