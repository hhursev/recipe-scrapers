from ._abstract import AbstractScraper


class PiesAndPlots(AbstractScraper):
    @classmethod
    def host(cls):
        return "piesandplots.net"
