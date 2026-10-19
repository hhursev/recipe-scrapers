from ._abstract import AbstractScraper


class PrimalEdgeHealth(AbstractScraper):
    @classmethod
    def host(cls):
        return "primaledgehealth.com"

    def ingredients(self):
        return [
            ingredient.replace("\u00c2", "") for ingredient in self.schema.ingredients()
        ]
