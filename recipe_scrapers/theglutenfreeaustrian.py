from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_yields


class TheGlutenFreeAustrian(AbstractScraper):
    @classmethod
    def host(cls):
        return "theglutenfreeaustrian.com"

    def ingredient_groups(self):
        ingredient_groups = group_ingredients(
            self.ingredients(),
            self.soup,
            ".mv-create-ingredients h4",
            ".mv-create-ingredients ul li",
        )

        schema_title = self.schema.title()

        for group in ingredient_groups:
            if group.purpose == schema_title:
                group.purpose = None

        return ingredient_groups

    def yields(self):
        yield_element = self.soup.select_one(".mv-create-title-wrap .mv-create-yield")
        return get_yields(yield_element)
