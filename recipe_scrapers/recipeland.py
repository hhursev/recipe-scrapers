from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup
from ._utils import normalize_string


class RecipeLand(AbstractScraper):
    @classmethod
    def host(cls):
        return "recipeland.com"

    def _parse_ingredient_row(self, row):
        """Helper method to parse ingredients."""
        amount = (
            row.select_one(".amount").get_text() if row.select_one(".amount") else ""
        )
        measure = (
            row.select_one(".measure").get_text() if row.select_one(".measure") else ""
        )
        ingredient = (
            row.select_one(".ingred").get_text() if row.select_one(".ingred") else ""
        )
        feature = (
            row.select_one(".ingred small").get_text()
            if row.select_one(".ingred small")
            else ""
        )

        full_ingredient = f"{amount} {measure} {ingredient}".strip()
        if feature:
            full_ingredient += f", {feature}"
        return normalize_string(full_ingredient)

    def ingredients(self):
        ingredients = []
        ingredient_rows = self.soup.select("#ingredient_list tbody tr")
        for row in ingredient_rows:
            if row.select_one("th.i-head"):
                continue

            full_ingredient = self._parse_ingredient_row(row)
            if full_ingredient:
                ingredients.append(full_ingredient)

        return ingredients

    def ingredient_groups(self):
        ingredient_rows = self.soup.select("#ingredient_list tbody tr")
        groups = []
        current_group = None
        grouped_ingredients = []

        for row in ingredient_rows:
            group_header = row.select_one("th.i-head")
            if group_header:
                if current_group or grouped_ingredients:
                    groups.append(
                        IngredientGroup(
                            ingredients=grouped_ingredients, purpose=current_group
                        )
                    )
                    grouped_ingredients = []

                current_group = group_header.get_text(strip=True)
                continue

            full_ingredient = self._parse_ingredient_row(row)
            if full_ingredient:
                grouped_ingredients.append(full_ingredient)

        if current_group or grouped_ingredients:
            groups.append(
                IngredientGroup(ingredients=grouped_ingredients, purpose=current_group)
            )

        return groups
