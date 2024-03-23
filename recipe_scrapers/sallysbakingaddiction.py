# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class SallysBakingAddiction(AbstractScraper):
    @classmethod
    def host(cls):
        return "sallysbakingaddiction.com"


    def description(self):
        return self.schema.description()

    def prep_time(self):
        return self.schema.prep_time()

    def cook_time(self):
        return self.schema.cook_time()
