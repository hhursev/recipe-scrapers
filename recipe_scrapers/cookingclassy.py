from ._abstract import AbstractScraper


class CookingClassy(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookingclassy.com"
