from ._abstract import AbstractScraper
from ._exceptions import StaticValueException
from ._grouping_utils import group_ingredients
from ._utils import normalize_string


class BongEats(AbstractScraper):
    @classmethod
    def host(cls):
        return "bongeats.com"

    def site_name(self):
        raise StaticValueException(return_value="Bong Eats")

    def ingredients(self):
        ingredients = self.soup.select(".recipe-ingredients ul li")
        return [normalize_string(i.get_text()) for i in ingredients]

    def instructions(self):
        instructions = self.soup.select(".recipe-process ol li")
        return "\n".join(normalize_string(i.get_text()) for i in instructions)

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".recipe-ingredients h3",
            ".recipe-ingredients ul li",
        )
