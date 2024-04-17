# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class PracticalSelfReliance(AbstractScraper):
    @classmethod
    def host(cls, domain="practicalselfreliance.com"):
        return domain
