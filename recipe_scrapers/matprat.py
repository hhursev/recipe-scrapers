from recipe_scrapers._grouping_utils import group_ingredients
from ._utils import normalize_string
from ._abstract import AbstractScraper
from ._exceptions import StaticValueException


class Matprat(AbstractScraper):
    @classmethod
    def host(cls):
        return "matprat.no"

    def site_name(self):
        raise StaticValueException(return_value="MatPrat")

    def ingredients(self):
        ingredient_list = []

        for li in self.soup.select(
            "li[class*='IngredientsGroup_ingredients-group__item']"
        ):
            parts = [
                normalize_string(span.get_text(" ", strip=True))
                for span in li.find_all("span")
            ]
            ingredient = " ".join(part for part in parts if part)
            if ingredient:
                ingredient_list.append(ingredient)

        return ingredient_list

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "h3[class*='IngredientsGroup_ingredients-group__title']",
            "li[class*='IngredientsGroup_ingredients-group__item']",
        )

    def nutrients(self):
        nutrient_names = [
            x.text for x in self.soup("td", "recipe-nutritions__table-cell-name")
        ]
        if not nutrient_names:
            return None
        nutrient_values = [
            x.text.replace("\xa0", " ")
            for x in self.soup("td", "recipe-nutritions__table-cell-value")
        ]
        return dict(zip(nutrient_names, nutrient_values))
