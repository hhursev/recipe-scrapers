# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class HeadbangersKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "headbangerskitchen.com"
