from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class AndyCooks(AbstractScraper):
    @classmethod
    def host(cls):
        return "andy-cooks.com"

    def site_name(self):
        return self.schema.site_name()

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def cook_time(self):
        return self.schema.cook_time()

    def prep_time(self):
        return self.schema.prep_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".rk_ingredients .rk_group_heading",
            ".rk_ingredients ul li",
        )

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def ratings_count(self):
        return self.schema.ratings_count()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()

    def keywords(self):
        return self.schema.keywords()
