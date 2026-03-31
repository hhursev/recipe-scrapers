from ._abstract import AbstractScraper


class DinnerAtTheZoo(AbstractScraper):
    @classmethod
    def host(cls):
        return "dinneratthezoo.com"
