from ._abstract import AbstractScraper


class Inspiralized(AbstractScraper):
    @classmethod
    def host(cls):
        return "inspiralized.com"
