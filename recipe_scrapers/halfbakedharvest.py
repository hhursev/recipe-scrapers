from ._abstract import AbstractScraper


class HalfBakedHarvest(AbstractScraper):
    @classmethod
    def host(cls):
        return "halfbakedharvest.com"
