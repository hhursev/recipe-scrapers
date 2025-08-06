from ._abstract import AbstractScraper


class ColleenChristensenNutrition(AbstractScraper):
    @classmethod
    def host(cls):
        return "colleenchristensennutrition.com"
