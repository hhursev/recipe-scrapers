from ._abstract import AbstractScraper


class Relish(AbstractScraper):
    @classmethod
    def host(cls):
        return "relish.com"
