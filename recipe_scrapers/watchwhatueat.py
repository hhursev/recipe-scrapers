from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class WatchWhatUEat(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "watchwhatueat.com"

    def ingredients(self):
        ingredients = []
        for element in self.soup.select(".wprm-recipe-ingredient"):
            parts = element.select(
                ".wprm-recipe-ingredient-amount, "
                ".wprm-recipe-ingredient-unit, "
                ".wprm-recipe-ingredient-name, "
                ".wprm-recipe-ingredient-notes"
            )
            text = " ".join(part.get_text(strip=True) for part in parts)
            ingredients.append(text.strip())
        return ingredients
