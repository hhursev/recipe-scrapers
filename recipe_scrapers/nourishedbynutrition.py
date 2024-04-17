# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class NourishedByNutrition(AbstractScraper):
    @classmethod
    def host(cls):
        return "nourishedbynutrition.com"

    def ratings(self):
        return self.schema.ratings()
