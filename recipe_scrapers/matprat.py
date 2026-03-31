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

        for ul in self.soup.select("div.recipe-ingredients ul.ingredientsList"):
            for li in ul.select("li[itemprop=ingredients]"):
                amount = li.find("span", class_="amount")
                unit = li.find("span", class_="unit")
                name = next(
                    (s for s in li.find_all("span") if s not in [amount, unit]), None
                )

                parts = []
                for tag in [amount, unit, name]:
                    if tag:
                        text = normalize_string(tag.get_text(separator=" ", strip=True))
                        if text:
                            parts.append(text)

                if parts:
                    ingredient_list.append(" ".join(parts))

        return ingredient_list

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup.find("div", "ingredients-list"),
            "h3.ingredient-section-title",
            "ul.ingredientsList > li > span:not(.amount):not(.unit)",
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
