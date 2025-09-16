from ._abstract import AbstractScraper


class BellyFull(AbstractScraper):
    @classmethod
    def host(cls):
        return "bellyfull.net"
