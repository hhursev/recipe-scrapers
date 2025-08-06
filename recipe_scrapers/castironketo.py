from ._abstract import AbstractScraper


class CastIronKeto(AbstractScraper):
    @classmethod
    def host(cls):
        return "castironketo.net"
