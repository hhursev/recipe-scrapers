# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class NYTimes(AbstractScraper):
    @classmethod
    def host(cls):
        return "cooking.nytimes.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def ingredient_groups(self):
        """
        The NYTimes website appears to auto generate it's CSS class names, which results in them ending
        with a string a random characters. Matching the exact class name is likely to break fairly quickly
        so instead we are going to match on a partial class name.
        For example, h3[class*='ingredientgroup_name'] matches an h3 element with a class that contains the value
        'ingredient_groupname' at least once anywhere in the element class attribute.
        See https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors
        """
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "h3[class*='ingredientgroup_name']",
            "li[class*='ingredient_ingredient']",
        )

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()
