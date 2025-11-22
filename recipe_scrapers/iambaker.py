from ._abstract import AbstractScraper


class IAmBaker(AbstractScraper):
    @classmethod
    def host(cls):
        return "iambaker.net"
