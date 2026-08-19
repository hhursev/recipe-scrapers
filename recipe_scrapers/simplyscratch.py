from ._abstract import AbstractScraper


class SimplyScratch(AbstractScraper):
    @classmethod
    def host(cls):
        return "simplyscratch.com"
