from ._abstract import AbstractScraper


class Lovingitvegan(AbstractScraper):
    @classmethod
    def host(cls):
        return "lovingitvegan.com"
