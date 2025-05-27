from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class NetaCooks(AbstractScraper):
    @classmethod
    def host(cls):
        return "netacooks.com"

    def ingredients(self):
        ing_list = []
        for ing_element in self.soup.select(".wprm-recipe-ingredient"):
            ing_name_element = ing_element.select_one(".wprm-recipe-ingredient-name")
            if not ing_name_element:
                continue

            bold_element = ing_name_element.select_one("strong")
            if bold_element and ing_name_element.get_text(
                strip=True
            ) == bold_element.get_text(strip=True):
                continue

            ing_list.append(ing_element.get_text(separator=" ", strip=True))
        return ing_list

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group-name, .wprm-recipe-ingredient-name strong",
            ".wprm-recipe-ingredient:not(:has(strong))",
        )
