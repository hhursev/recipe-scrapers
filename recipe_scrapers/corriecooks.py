from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup


class CorrieCooks(AbstractScraper):
    @classmethod
    def host(cls):
        return "corriecooks.com"

    def _parse_ingredient(self, ingredient):
        name = ingredient.select_one(".wprm-recipe-ingredient-name")
        if not name:
            return None, None

        is_heading = (
            not ingredient.select_one(".wprm-recipe-ingredient-amount")
            and not ingredient.select_one(".wprm-recipe-ingredient-unit")
            and name.get_text(strip=True).endswith(":")
        )

        text = " ".join(
            el.get_text(" ", strip=True)
            for el in ingredient.select(
                ".wprm-recipe-ingredient-amount, "
                ".wprm-recipe-ingredient-unit, "
                ".wprm-recipe-ingredient-name, "
                ".wprm-recipe-ingredient-notes"
            )
        ).strip()

        return text, is_heading

    def ingredients(self):
        items = []

        for ingredient in self.soup.select(".wprm-recipe-ingredient"):
            text, is_heading = self._parse_ingredient(ingredient)
            if text and not is_heading:
                items.append(text)

        return items

    def ingredient_groups(self):
        groups = []
        current_group = None

        for ingredient in self.soup.select(".wprm-recipe-ingredient"):
            text, is_heading = self._parse_ingredient(ingredient)
            if not text:
                continue

            if is_heading:
                current_group = IngredientGroup(
                    purpose=text,
                    ingredients=[],
                )
                groups.append(current_group)
                continue

            if current_group is None:
                current_group = IngredientGroup(
                    purpose=None,
                    ingredients=[],
                )
                groups.append(current_group)

            current_group.ingredients.append(text)

        return groups
