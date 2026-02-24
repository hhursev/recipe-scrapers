from ._abstract import AbstractScraper


class NutritionFacts(AbstractScraper):
    @classmethod
    def host(cls):
        return "nutritionfacts.org"
