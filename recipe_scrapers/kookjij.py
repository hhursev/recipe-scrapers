from ._abstract import AbstractScraper
from ._utils import normalize_string


class KookJij(AbstractScraper):
    @classmethod
    def host(cls):
        return "kookjij.nl"

    def ingredients(self):
        ingredients_elements = self.soup.select(
            ".checkbox span[itemprop='ingredients']"
        )
        ingredients_list = [
            ingredient.get_text() for ingredient in ingredients_elements
        ]
        return [normalize_string(ingredient) for ingredient in ingredients_list]

    def equipment(self):
        equipment_elements = self.soup.select(".recipe-accessoires .checkbox label")
        equipment_list = [
            equipment.get_text(strip=True) for equipment in equipment_elements
        ]
        return equipment_list

    def category(self):
        return ", ".join(
            category.get_text(strip=True)
            for category in self.soup.select(
                ".categories li[itemprop='recipeCategory'] a"
            )
        )

    def cuisine(self):
        cuisine_element = self.soup.select_one('.row [itemprop="recipeCuisine"]')
        return cuisine_element.get_text(strip=True) if cuisine_element else None
