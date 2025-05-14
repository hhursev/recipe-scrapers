from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import normalize_string


class SizzleFish(AbstractScraper):
    @classmethod
    def host(cls):
        return "sizzlefish.com"

    def description(self):
        description_div = self.soup.find("div", class_="rk_description")
        if description_div:
            next_element = description_div.find_next()
            if next_element:
                return next_element.get_text(strip=True)

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".rk_group_heading",
            ".rk_ingredients li",
        )

    def category(self):
        return normalize_string(self.schema.category())
