from ._abstract import AbstractScraper


class CulinaryHill(AbstractScraper):
    @classmethod
    def host(cls):
        return "culinaryhill.com"
