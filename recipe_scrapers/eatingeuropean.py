from ._abstract import AbstractScraper


class EatingEuropean(AbstractScraper):
    @classmethod
    def host(cls):
        return "eatingeuropean.com"
