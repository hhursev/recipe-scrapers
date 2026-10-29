from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup


class CdKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "cdkitchen.com"

    def ingredients(self):
        ingredients = []
        for el in self.soup.select('p.ml-30 span[itemprop="recipeIngredient"]'):
            if el.select_one("span.uline.big2"):
                continue
            text = " ".join(el.get_text(strip=True).split())
            ingredients.append(text)
        return ingredients

    def ingredient_groups(self):
        groups = []
        current_group = None

        for el in self.soup.select('p.ml-30 span[itemprop="recipeIngredient"]'):
            heading = el.select_one("span.uline.big2")

            if heading:
                if current_group:
                    groups.append(current_group)
                purpose = " ".join(el.get_text(strip=True).split())
                current_group = IngredientGroup(ingredients=[], purpose=purpose)
            else:
                if current_group is None:
                    current_group = IngredientGroup(ingredients=[], purpose=None)
                text = " ".join(el.get_text(strip=True).split())
                current_group.ingredients.append(text)

        if current_group:
            groups.append(current_group)

        return groups
