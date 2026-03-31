from ._abstract import AbstractScraper
from ._utils import normalize_string
from ._grouping_utils import group_ingredients


class VarechaPravdaSK(AbstractScraper):
    @classmethod
    def host(cls):
        return "varecha.pravda.sk"

    def _format_ingredient(self, element):
        ingredient_name = normalize_string(
            element.find("td", class_="recipe-ingredients__ingredient").text
        )
        ingredient_amount = normalize_string(
            element.find("td", class_="recipe-ingredients__amount").text
        )

        if ingredient_amount:
            return f"{ingredient_amount} {ingredient_name}"
        return ingredient_name

    def ingredients(self):
        return [
            self._format_ingredient(row)
            for row in self.soup.select("div.suroviny table tr.recipe-ingredients__row")
        ]

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".recipe-ingredients__group",
            ".recipe-ingredients__row",
        )
