from ._abstract import AbstractScraper


class Godt(AbstractScraper):
    @classmethod
    def host(cls):
        return "godt.no"

    def yields(self):
        return self.schema.yields()

    def ratings(self):
        return self.schema.ratings()
