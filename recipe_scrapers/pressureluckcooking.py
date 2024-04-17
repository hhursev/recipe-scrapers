# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class PressureLuckCooking(AbstractScraper):
    @classmethod
    def host(cls):
        return "pressureluckcooking.com"

    def category(self):
        return self.schema.category()
