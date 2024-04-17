# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class PurpleCarrot(AbstractScraper):
    @classmethod
    def host(cls):
        return "purplecarrot.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def nutrients(self):
        return self.schema.nutrients()
