# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class WhatsGabyCooking(AbstractScraper):
    @classmethod
    def host(cls):
        return "whatsgabycooking.com"

    def yields(self):
        return self.schema.yields()
