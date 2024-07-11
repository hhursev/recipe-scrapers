from ._abstract import AbstractScraper


class TheVintageMixer(AbstractScraper):
    @classmethod
    def host(cls):
        return "thevintagemixer.com"
