from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup
from ._utils import normalize_string


class PickUpLimes(AbstractScraper):
    @classmethod
    def host(cls):
        return "pickuplimes.com"

    def ingredients(self):
        return [
            el.get_text(separator=" ", strip=True)
            for el in self.soup.select("div.ingredient-container")
        ]

    def ingredient_groups(self):
        groups = []
        current_purpose = None
        current_ingredients = []

        for element in self.soup.select("h3.pt-3, div.ingredient-container"):
            if element.name == "h3":
                if current_ingredients:
                    groups.append(
                        IngredientGroup(
                            ingredients=current_ingredients, purpose=current_purpose
                        )
                    )
                    current_ingredients = []
                current_purpose = element.get_text(strip=True)
            elif element.name == "div" and "ingredient-container" in element.get(
                "class", []
            ):
                text = element.get_text(separator=" ", strip=True)
                current_ingredients.append(text)

        if current_ingredients:
            groups.append(
                IngredientGroup(
                    ingredients=current_ingredients, purpose=current_purpose
                )
            )

        if not groups:
            return [IngredientGroup(ingredients=self.ingredients())]

        return groups

    def instructions(self):
        instructions = [
            normalize_string(e.get_text())
            for e in self.soup.find_all(class_="direction")
        ]
        return "\n".join(instructions) if instructions else None
