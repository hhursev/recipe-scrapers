from ._abstract import AbstractScraper


class FoodNetwork(AbstractScraper):
    @classmethod
    def host(cls):
        return "foodnetwork.co.uk"

    def author(self):
        return self.schema.author()

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

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
