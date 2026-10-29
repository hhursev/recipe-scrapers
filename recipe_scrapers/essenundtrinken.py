from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup


class EssenUndTrinken(AbstractScraper):
    @classmethod
    def host(cls):
        return "essen-und-trinken.de"

    def ingredients(self):
        ingredients = []

        for label in self.soup.select(".recipe-ingredients__label"):
            amount = label.find_previous_sibling("x-beautify-number")
            amount_text = amount.get_text(" ", strip=True) if amount else ""
            label_text = label.get_text(" ", strip=True)

            ingredient = " ".join(filter(None, [amount_text, label_text]))
            ingredients.append(ingredient)

        return ingredients

    def ingredient_groups(self):
        container = self.soup.select_one(".recipe-ingredients__list")

        if not container:
            return [IngredientGroup(ingredients=self.ingredients(), purpose=None)]

        separators = container.select(".recipe-ingredients__separator")

        if not separators:
            return [IngredientGroup(ingredients=self.ingredients(), purpose=None)]

        groups = []
        purpose = None
        ingredients = []

        for element in container.children:
            if not getattr(element, "name", None):
                continue

            if "recipe-ingredients__separator" in element.get("class", []):
                if purpose is not None and ingredients:
                    groups.append(
                        IngredientGroup(
                            ingredients=ingredients,
                            purpose=purpose,
                        )
                    )

                heading = element.select_one("p")
                purpose = heading.get_text(" ", strip=True) if heading else None
                ingredients = []

            elif element.name == "x-beautify-number":
                amount = element.get_text(" ", strip=True)
                label = element.find_next_sibling(
                    "p", class_="recipe-ingredients__label"
                )

                if label:
                    ingredient = " ".join(
                        filter(
                            None,
                            [
                                amount,
                                label.get_text(" ", strip=True),
                            ],
                        )
                    )
                    ingredients.append(ingredient)

        if purpose is not None and ingredients:
            groups.append(
                IngredientGroup(
                    ingredients=ingredients,
                    purpose=purpose,
                )
            )

        return groups
