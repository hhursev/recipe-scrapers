# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Lovingitvegan(AbstractScraper):
    @classmethod
    def host(cls):
        return "lovingitvegan.com"

    def title(self):
        return self.schema.title()

    def description(self):
        return self.schema.description()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def ratings(self):
        return self.schema.ratings()
