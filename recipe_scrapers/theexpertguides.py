# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class TheExpertGuides(AbstractScraper):
    @classmethod
    def host(cls):
        return "theexpertguides.com"

    def cuisine(self):
        return self.schema.cuisine()
