from ._abstract import AbstractScraper


class FoodNetwork(AbstractScraper):
    @classmethod
    def host(cls):
        return "foodnetwork.co.uk"

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
