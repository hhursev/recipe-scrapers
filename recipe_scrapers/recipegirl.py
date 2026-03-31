from ._abstract import AbstractScraper


class RecipeGirl(AbstractScraper):
    @classmethod
    def host(cls):
        return "recipegirl.com"
