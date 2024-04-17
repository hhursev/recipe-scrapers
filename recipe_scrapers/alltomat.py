# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class AllTomat(AbstractScraper):
    @classmethod
    def host(cls):
        return "alltommat.se"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".ingredients-section h2",
            ".ingredients-list li",
        )

    def ratings(self):
        return self.schema.ratings()
