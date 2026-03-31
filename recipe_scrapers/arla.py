from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup


class Arla(AbstractScraper):
    @classmethod
    def host(cls):
        return "arla.se"

    def ingredients(self):
        ingredients = []
        for row in self.soup.select(".c-recipe__ingredients-group tr"):
            name_el = row.select_one("th")
            amount_el = row.select_one("td")

            name = name_el.get_text(strip=True) if name_el else ""
            amount = amount_el.get_text(strip=True) if amount_el else ""

            ingredient = f"{amount} {name}".strip()
            if ingredient:
                ingredients.append(ingredient)

        return ingredients

    def ingredient_groups(self):

        groups = []
        for group in self.soup.select(".c-recipe__ingredients-group"):
            heading_tag = group.select_one("h3")
            purpose = heading_tag.get_text(strip=True) if heading_tag else None

            ingredients = []
            for row in group.select("tr"):
                name_el = row.select_one("th")
                amount_el = row.select_one("td")

                name = name_el.get_text(strip=True) if name_el else ""
                amount = amount_el.get_text(strip=True) if amount_el else ""

                # Capitalize only the first letter of the name part
                if name:
                    name = name[0].upper() + name[1:]

                ingredient = f"{amount} {name}".strip()
                if ingredient:
                    ingredients.append(ingredient)

            if ingredients:
                groups.append(IngredientGroup(ingredients=ingredients, purpose=purpose))

        return groups
