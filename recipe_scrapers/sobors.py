# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class SoBors(AbstractScraper):
    @classmethod
    def host(cls):
        return "sobors.hu"
