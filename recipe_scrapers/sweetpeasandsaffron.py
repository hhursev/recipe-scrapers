# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class SweetPeasAndSaffron(AbstractScraper):
    """
    Web scraper for Sweet Peas & Saffron website
    """

    @classmethod
    def host(cls):
        return "sweetpeasandsaffron.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def instructions(self):
        return self.schema.instructions()

    def ingredients(self):
        return self.schema.ingredients()

    def ratings(self):
        return self.schema.ratings()

    def author(self):
        return self.schema.author()
