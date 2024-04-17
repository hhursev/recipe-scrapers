# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Cucchiaio(AbstractScraper):
    @classmethod
    def host(cls):
        return "cucchiaio.it"

    def title(self):
        return self.schema.title()
