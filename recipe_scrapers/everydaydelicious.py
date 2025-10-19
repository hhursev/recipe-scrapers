from ._abstract import AbstractScraper


class EverydayDelicious(AbstractScraper):
    @classmethod
    def host(cls):
        return "everyday-delicious.com"
