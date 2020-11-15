from ._abstract import AbstractScraper


class ArchanasKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "archanaskitchen.com"

    def title(self):
        return self.schema.title()

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
