from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup


class CleanEatingKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "cleaneatingkitchen.com"

    def ingredient_groups(self):
        groups = []
        current_group = None

        for li in self.soup.select(".tasty-recipes-ingredients li"):
            heading = li.select_one("strong em")
            if heading:
                current_group = IngredientGroup(
                    ingredients=[], purpose=heading.get_text(strip=True)
                )
                groups.append(current_group)
            else:
                if current_group is None:
                    current_group = IngredientGroup(ingredients=[], purpose=None)
                    groups.append(current_group)
                current_group.ingredients.append(li.get_text(" ", strip=True))

        return groups
