from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class CountryLiving(AbstractScraper):
    @classmethod
    def host(cls):
        return "countryliving.com"

    def author(self):
        return self.schema.author() or "Country Living"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".ingredients-body h3",
            ".ingredients-body li",
        )

    def keywords(self):
        keywords = self.schema.keywords()
        filtered_keywords = [kw for kw in keywords if ": " not in kw]
        return filtered_keywords
