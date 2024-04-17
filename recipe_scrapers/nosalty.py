from ._abstract import AbstractScraper


class NoSalty(AbstractScraper):
    @classmethod
    def host(cls):
        return "nosalty.hu"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def ratings(self):
        return self.schema.ratings()
