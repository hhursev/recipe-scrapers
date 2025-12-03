from ._abstract import AbstractScraper


class ColeyCooks(AbstractScraper):
    @classmethod
    def host(cls):
        return "coleycooks.com"
