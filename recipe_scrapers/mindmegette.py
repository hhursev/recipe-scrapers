from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class Mindmegette(AbstractScraper):
    @classmethod
    def host(cls):
        return "www.mindmegette.hu"

    def title(self):
        return self.soup.find("h1", {"class": "title"}).get_text()

    def total_time(self):
        item_sibling = self.soup.find("span", {"class": "spriteTime"})
        time = item_sibling.find_next().get_text()

        return get_minutes(time)

    def image(self):
        image_relative_url = self.soup.find("img", {"itemprop": "image", "src": True})[
            "src"
        ]

        if image_relative_url is not None:
            image_relative_url = f"https://{self.host()}{image_relative_url}"

        return image_relative_url

    def ingredients(self):
        ingredients = []
        shopping_cart = self.soup.find("ul", {"class": "shopingCart"}).findAll("li")

        for ingredient in shopping_cart:
            amount_unit = (
                ingredient.find("span", {"class": "ingredient-measure"})
                .get("title")
                .strip()
            )
            ingredient_name = (
                ingredient.find("span", {"class": "ingredient-name"}).get_text().strip()
            )
            ingredients.append((amount_unit + " " + ingredient_name).strip())

        return ingredients

    def instructions(self):
        instructions = self.soup.find("div", {"class": "instructions"}).findAll("li")

        instructions_arr = []
        for instruction in instructions:
            for tag in instruction.findAll("h2"):
                tag.replaceWith("")
            instructions_arr.append(normalize_string(instruction.get_text()))

        return "\n".join(instructions_arr)

    def yields(self):
        item_sibling = self.soup.find("span", {"class": "spritePortion"})
        portion = item_sibling.find_next().get_text()

        return get_yields(portion)
