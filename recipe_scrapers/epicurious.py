# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class Epicurious(AbstractScraper):
    @classmethod
    def host(cls):
        return "epicurious.com"

    def title(self):
        return self.schema.title()

    def author(self):
        return self.soup.find("a", {"itemprop": "author"}).get_text()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def ratings(self):
        return self.schema.ratings()
