# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class CookPad(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookpad.com"
