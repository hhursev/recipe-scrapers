# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class CastIronKeto(AbstractScraper):
    @classmethod
    def host(cls):
        return "castironketo.net"
