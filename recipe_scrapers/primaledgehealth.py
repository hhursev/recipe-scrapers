from ._abstract import AbstractScraper


class PrimalEdgeHealth(AbstractScraper):
    @classmethod
    def host(cls):
        return "primaledgehealth.com"

    def ingredients(self):
        return [
            ingredient.replace("\u00C2", "") for ingredient in self.schema.ingredients()
        ]
