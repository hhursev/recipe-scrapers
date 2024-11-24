from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup
from ._utils import normalize_string


class RecipeLand(AbstractScraper):
    @classmethod
    def host(cls):
        return "recipeland.com"

    def _parse_ingredient_row(self, row):
        amount = row.select_one(".amount") and row.select_one(".amount").get_text()
        measure = row.select_one(".measure") and row.select_one(".measure").get_text()
        ingredient_elem = row.select_one(".ingred")
        ingredient = ingredient_elem and ingredient_elem.get_text()
        feature = (
            ingredient_elem
            and ingredient_elem.select_one("small")
            and ingredient_elem.select_one("small").get_text()
        )

        full_ingredient = f"{amount} {measure} {ingredient}".strip()
        if feature:
            full_ingredient += f", {feature}"
        return normalize_string(full_ingredient)

    def ingredients(self):
        ingredient_rows = self.soup.select("#ingredient_list tbody tr")
        return [
            self._parse_ingredient_row(row)
            for row in ingredient_rows
            if not row.select_one("th.i-head")
        ]

    def ingredient_groups(self):

        def add_group():
            if current_group or grouped_ingredients:
                groups.append(
                    IngredientGroup(
                        ingredients=grouped_ingredients, purpose=current_group
                    )
                )

        ingredient_rows = self.soup.select("#ingredient_list tbody tr")
        groups = []
        current_group = None
        grouped_ingredients = []

        for row in ingredient_rows:
            group_header = row.select_one("th.i-head")
            if group_header:
                add_group()
                grouped_ingredients = []
                current_group = group_header.get_text(strip=True)
            else:
                full_ingredient = self._parse_ingredient_row(row)
                if full_ingredient:
                    grouped_ingredients.append(full_ingredient)

        add_group()
        return groups
