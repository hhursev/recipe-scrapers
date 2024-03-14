# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class SundPaaBudget(AbstractScraper):
    @classmethod
    def host(cls):
        return "sundpaabudget.dk"

    def cook_time(self):
        return self.schema.cook_time()

    def prep_time(self):
        return self.schema.prep_time()

    def description(self):
        # Schema returns empty string
        return self.soup.head.find("meta", {"property": "og:description"})["content"]
