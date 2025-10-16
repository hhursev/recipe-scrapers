from ._abstract import AbstractScraper


class AmericasTestKitchen(AbstractScraper):

    @classmethod
    def host(cls):
        return "americastestkitchen.com"

    def ingredients(self):
        return [
            ingredient.replace(" ,", ",") for ingredient in self.schema.ingredients()
        ]
