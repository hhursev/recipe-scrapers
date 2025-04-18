from ._abstract import AbstractScraper
from ._utils import normalize_string
from ._grouping_utils import IngredientGroup


class AHealthySliceOfLife(AbstractScraper):
    @classmethod
    def host(cls):
        return "ahealthysliceoflife.com"

    def ingredients(self):
        ingredients = []
        for p in self.soup.select(".tasty-recipes-ingredients-body p"):
            if not p.find("strong"):
                text = p.get_text(" ", strip=True)
                if text:
                    ingredients.append(normalize_string(text))
        return ingredients

    def ingredient_groups(self):
        groups = []
        current_purpose = None
        current_ingredients = []

        for p in self.soup.select(".tasty-recipes-ingredients-body p"):
            text = p.get_text(" ", strip=True)
            if not text:
                continue
            if p.find("strong"):
                if current_ingredients:
                    groups.append(
                        IngredientGroup(
                            ingredients=current_ingredients, purpose=current_purpose
                        )
                    )
                current_purpose = text
                current_ingredients = []
            else:
                current_ingredients.append(text)

        if current_ingredients:
            groups.append(
                IngredientGroup(
                    ingredients=current_ingredients, purpose=current_purpose
                )
            )

        return groups
