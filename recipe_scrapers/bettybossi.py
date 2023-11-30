# mypy: disallow_untyped_defs=False

from ._abstract import AbstractScraper


class BettyBossi(AbstractScraper):
    """Scrape BettyBossi.ch recipes.

    This scraper is particular as the website implements a refresh after
    loading the page the first time. It is therefore needed to do two get
    requests in a single session, once to initialize the connection, the second
    to load the page content.
    """

    @classmethod
    def host(cls):
        return "bettybossi.ch"

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
