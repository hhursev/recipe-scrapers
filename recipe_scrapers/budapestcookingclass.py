from ._abstract import AbstractScraper
from ._wprm import WPRMMixin
from ._grouping_utils import IngredientGroup


class BudapestCookingClass(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "budapestcookingclass.com"

    def image(self):
        image = self.soup.select_one(
            ".fusion-text img.wp-image-5808, .fusion-text p img"
        )
        if image:
            return image.get("data-orig-src") or image.get("src")

    def ingredients(self):
        container = self.soup.select_one(".wprm-recipe-ingredients-container")
        if not container:
            return []

        ingredients = []

        for item in container.select("li.wprm-recipe-ingredient"):
            parts = []

            for class_name in (
                "amount",
                "unit",
                "name",
                "notes",
            ):
                element = item.select_one(f".wprm-recipe-ingredient-{class_name}")
                if element:
                    value = element.get_text(" ", strip=True)
                    if value:
                        parts.append(f"({value})" if class_name == "notes" else value)

            if parts:
                ingredients.append(" ".join(parts))

        return ingredients

    def ingredient_groups(self):
        ingredients = self.ingredients()
        container = self.soup.select_one(".wprm-recipe-ingredients-container")

        if not container:
            return [IngredientGroup(ingredients=ingredients, purpose=None)]

        groups = []
        remaining = ingredients.copy()

        for group in container.select(".wprm-recipe-ingredient-group"):
            heading = group.select_one(".wprm-recipe-ingredient-group-name")
            purpose = heading.get_text(" ", strip=True) if heading else None

            group_items = []

            for item in group.select("li.wprm-recipe-ingredient"):
                parts = []

                for class_name in ("amount", "unit", "name", "notes"):
                    element = item.select_one(f".wprm-recipe-ingredient-{class_name}")
                    if element:
                        value = element.get_text(" ", strip=True)
                        if value:
                            parts.append(
                                f"({value})" if class_name == "notes" else value
                            )

                ingredient = " ".join(parts)

                if ingredient in remaining:
                    group_items.append(ingredient)
                    remaining.remove(ingredient)

            if group_items:
                groups.append(IngredientGroup(ingredients=group_items, purpose=purpose))

        if remaining:
            if groups:
                groups[-1].ingredients.extend(remaining)
            else:
                groups.append(IngredientGroup(ingredients=remaining, purpose=None))

        return groups or [IngredientGroup(ingredients=ingredients, purpose=None)]
