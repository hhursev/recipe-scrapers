from ._abstract import AbstractScraper
from ._utils import normalize_string


class DrizzleAndDip(AbstractScraper):
    @classmethod
    def host(cls):
        return "drizzleanddip.com"

    def ingredients(self):
        ingredients_list = []
        for el in self.soup.select(".wprm-recipe-ingredient"):
            amount = el.select_one(".wprm-recipe-ingredient-amount")
            unit = el.select_one(".wprm-recipe-ingredient-unit")
            name = el.select_one(".wprm-recipe-ingredient-name")
            notes = el.select_one(".wprm-recipe-ingredient-notes")

            ingredient_parts = [
                amount.get_text(strip=True) if amount else None,
                unit.get_text(strip=True) if unit else None,
                name.get_text(strip=True) if name else None,
                notes.get_text(strip=True) if notes else None,
            ]

            ingredient = " ".join(filter(None, ingredient_parts))
            ingredients_list.append(normalize_string(ingredient))

        return ingredients_list

    def instructions(self):
        instructions = self.soup.find_all(
            "div", {"class": "wprm-recipe-instruction-text"}
        )

        instructions = [normalize_string(i.get_text()) for i in instructions]
        return "\n".join(instructions)
