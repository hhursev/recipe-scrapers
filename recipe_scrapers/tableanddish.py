from ._abstract import AbstractScraper


class TableAndDish(AbstractScraper):
    @classmethod
    def host(cls):
        return "tableanddish.com"
