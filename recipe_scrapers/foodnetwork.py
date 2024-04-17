from ._abstract import AbstractScraper


class FoodNetwork(AbstractScraper):
    @classmethod
    def host(cls, domain="co.uk"):
        return f"foodnetwork.{domain}"

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
