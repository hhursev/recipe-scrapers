from ._abstract import AbstractScraper


class IndianHealthyRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "indianhealthyrecipes.com"
