from ._abstract import AbstractScraper


class EatingWell(AbstractScraper):
    @classmethod
    def host(cls):
        return "eatingwell.com"
