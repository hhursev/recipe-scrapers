# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Lovingitvegan(AbstractScraper):
    @classmethod
    def host(cls):
        return "lovingitvegan.com"
