# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class PressureLuckCooking(AbstractScraper):
    @classmethod
    def host(cls):
        return "pressureluckcooking.com"

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
