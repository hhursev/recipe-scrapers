# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class Vegolosi(AbstractScraper):
    @classmethod
    def host(cls):
        return "vegolosi.it"

    def title(self):
        return self.soup.h1.get_text().strip()

    def author(self):
        return self.schema.author()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()
