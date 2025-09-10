from ._abstract import AbstractScraper
from ._utils import normalize_string
from ._grouping_utils import normalize_fractions


class ItDoesntTasteLikeChicken(AbstractScraper):
    @classmethod
    def host(cls):
        return "itdoesnttastelikechicken.com"

    def ingredients(self):
        ingredients = []
        for li in self.soup.select(".wprm-recipe-ingredients li"):
            amount = li.select_one(".wprm-recipe-ingredient-amount")
            unit = li.select_one(".wprm-recipe-ingredient-unit")
            name = li.select_one(".wprm-recipe-ingredient-name")
            notes = li.select_one(".wprm-recipe-ingredient-notes")

            parts = []
            if amount:
                amt_text = normalize_fractions(amount.get_text())
                parts.append(amt_text)
            if unit:
                parts.append(unit.get_text())
            if name:
                parts.append(name.get_text())
            if notes and parts:
                parts[-1] += f" ({notes.get_text()})"

            if parts:
                ingredient_str = " ".join(parts)
                ingredients.append(normalize_string(ingredient_str))

        return ingredients
