from ._abstract import AbstractScraper


class NewDadsKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "newdadskitchen.com"
