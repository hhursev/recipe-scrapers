# mypy: disallow_untyped_defs=False

from ._abstract import AbstractScraper


class GreatBritishChefs(AbstractScraper):
    @classmethod
    def host(cls):
        return "greatbritishchefs.com"

    def description(self):
        return self.schema.description()
