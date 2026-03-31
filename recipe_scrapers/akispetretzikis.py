from ._abstract import AbstractScraper


class AkisPetretzikis(AbstractScraper):
    @classmethod
    def host(cls):
        return "akispetretzikis.com"
