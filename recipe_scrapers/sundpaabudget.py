# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class SundPaaBudget(AbstractScraper):
    @classmethod
    def host(cls):
        return "sundpaabudget.dk"

    def category(self):
        return self.schema.category()

    def description(self):
        # Schema returns empty string
        return self.soup.head.find("meta", {"property": "og:description"})["content"]
