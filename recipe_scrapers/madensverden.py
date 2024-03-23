# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class MadensVerden(AbstractScraper):
    @classmethod
    def host(cls):
        return "madensverden.dk"

    def cook_time(self):
        return self.schema.cook_time()

    def prep_time(self):
        return self.schema.prep_time()
