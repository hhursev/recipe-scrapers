from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup
from ._utils import normalize_string


class VelocidadCuchara(AbstractScraper):
    @classmethod
    def host(cls):
        return "velocidadcuchara.com"

    def _ingredient_items(self):
        return self.soup.select(".ERSIngredients li.ingredient")

    def _is_group_header(self, li):
        strong = li.find("strong")
        return bool(
            strong
            and normalize_string(li.get_text()) == normalize_string(strong.get_text())
        )

    def ingredients(self):
        return [
            normalize_string(li.get_text())
            for li in self._ingredient_items()
            if not self._is_group_header(li)
        ]

    def ingredient_groups(self):
        groups = []
        current_purpose = None
        current_ingredients = []

        for li in self._ingredient_items():
            text = normalize_string(li.get_text())
            if self._is_group_header(li):
                if current_ingredients:
                    groups.append(
                        IngredientGroup(
                            purpose=current_purpose, ingredients=current_ingredients
                        )
                    )
                current_purpose = text.rstrip(":")
                current_ingredients = []
            else:
                current_ingredients.append(text)

        if current_ingredients:
            groups.append(
                IngredientGroup(
                    purpose=current_purpose, ingredients=current_ingredients
                )
            )

        return groups or [IngredientGroup(purpose=None, ingredients=self.ingredients())]
