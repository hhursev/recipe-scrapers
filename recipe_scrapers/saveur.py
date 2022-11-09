# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Saveur(AbstractScraper):
    @classmethod
    def host(cls):
        return "saveur.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.soup.find("h1").get_text()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()
