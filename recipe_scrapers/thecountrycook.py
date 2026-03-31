from ._abstract import AbstractScraper


class TheCountryCook(AbstractScraper):
    @classmethod
    def host(cls):
        return "thecountrycook.net"
