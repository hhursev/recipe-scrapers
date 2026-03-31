from ._abstract import AbstractScraper


class FitSlowCookerQueen(AbstractScraper):
    @classmethod
    def host(cls):
        return "fitslowcookerqueen.com"
