from ._abstract import AbstractScraper


class ErinLivesWhole(AbstractScraper):
    @classmethod
    def host(cls):
        return "erinliveswhole.com"
