from ._abstract import AbstractScraper


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
