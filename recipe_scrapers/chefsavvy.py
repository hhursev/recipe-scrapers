from ._abstract import AbstractScraper


class ChefSavvy(AbstractScraper):
    @classmethod
    def host(cls):
        return "chefsavvy.com"
