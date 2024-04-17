# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class SweetPeasAndSaffron(AbstractScraper):
    """
    Web scraper for Sweet Peas & Saffron website
    """

    @classmethod
    def host(cls):
        return "sweetpeasandsaffron.com"

    def ratings(self):
        return self.schema.ratings()
