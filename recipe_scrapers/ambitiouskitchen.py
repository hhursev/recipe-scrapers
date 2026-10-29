from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup


class AmbitiousKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "ambitiouskitchen.com"

    def ingredients(self):
        ingredients = []

        for li in self.soup.select(".wprm-recipe-ingredient"):
            name_tag = li.select_one(".wprm-recipe-ingredient-name")
            amount = li.select_one(".wprm-recipe-ingredient-amount")
            unit = li.select_one(".wprm-recipe-ingredient-unit")

            is_group_header = (
                name_tag is not None
                and name_tag.find("strong") is not None
                and amount is None
                and unit is None
            )

            if is_group_header:
                continue

            text = li.get_text(" ", strip=True)
            ingredients.append(text)

        return ingredients

    def ingredient_groups(self):
        groups = []
        current_purpose = None
        current_ingredients = []

        for li in self.soup.select(".wprm-recipe-ingredient"):
            name_tag = li.select_one(".wprm-recipe-ingredient-name")
            amount = li.select_one(".wprm-recipe-ingredient-amount")
            unit = li.select_one(".wprm-recipe-ingredient-unit")

            is_group = (
                name_tag is not None
                and name_tag.find("strong") is not None
                and amount is None
                and unit is None
            )

            if is_group:
                if current_ingredients:
                    groups.append(
                        IngredientGroup(
                            ingredients=current_ingredients,
                            purpose=current_purpose,
                        )
                    )
                    current_ingredients = []

                current_purpose = name_tag.get_text(strip=True)
                continue

            current_ingredients.append(li.get_text(" ", strip=True))

        if current_ingredients:
            groups.append(
                IngredientGroup(
                    ingredients=current_ingredients,
                    purpose=current_purpose,
                )
            )

        return groups
