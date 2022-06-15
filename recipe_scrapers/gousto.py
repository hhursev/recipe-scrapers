from ._abstract import AbstractScraper


# TODO: Remove? Switching over to GoustoJson 2022-08-01
class Gousto(AbstractScraper):
    @classmethod
    def host(cls):
        return "gousto.co.uk"

    def title(self):
        return self.schema.title()

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
