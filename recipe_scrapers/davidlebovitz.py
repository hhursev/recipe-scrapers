# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class DavidLebovitz(AbstractScraper):
    @classmethod
    def host(cls):
        return "davidlebovitz.com"
