# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class PurpleCarrot(AbstractScraper):
    @classmethod
    def host(cls):
        return "purplecarrot.com"
