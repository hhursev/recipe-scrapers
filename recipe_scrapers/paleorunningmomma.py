# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class PaleoRunningMomma(AbstractScraper):
    @classmethod
    def host(cls):
        return "paleorunningmomma.com"
