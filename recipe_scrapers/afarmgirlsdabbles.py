from ._abstract import AbstractScraper


class AFarmGirlsDabbles(AbstractScraper):
    @classmethod
    def host(cls):
        return "afarmgirlsdabbles.com"

    def ingredients(self):
        ingredients = []
        for element in self.soup.select(".wprm-recipe-ingredient"):
            parts = element.select(
                ".wprm-recipe-ingredient-amount, "
                ".wprm-recipe-ingredient-unit, "
                ".wprm-recipe-ingredient-name, "
                ".wprm-recipe-ingredient-notes"
            )
            text = " ".join(
                part.get_text(strip=True) for part in parts if part.get_text(strip=True)
            )
            ingredients.append(text.strip())
        return ingredients
