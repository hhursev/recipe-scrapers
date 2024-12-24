from ._abstract import AbstractScraper


class NourishedByNutrition(AbstractScraper):
    @classmethod
    def host(cls):
        return "nourishedbynutrition.com"
