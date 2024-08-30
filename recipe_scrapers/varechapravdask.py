from ._abstract import AbstractScraper


class VarechaPravdaSK(AbstractScraper):
    @classmethod
    def host(cls):
        return "varecha.pravda.sk"
