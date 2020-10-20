from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class Mindmegette(AbstractScraper):
    @classmethod
    def host(cls):
        return "mindmegette.hu"

    def title(self):
        return self.soup.find("h1", {"class": "title"}).get_text()

    def total_time(self):
        return get_minutes(self.soup.find("span", {"class": "time"}))

    def image(self):
        image_relative_url = self.soup.find("img", {"itemprop": "photo", "src": True})[
            "src"
        ]

        if image_relative_url is not None:
            image_relative_url = f"http://{self.host()}{image_relative_url}"

        return image_relative_url

    def ingredients(self):
        ingredients_html = self.soup.findAll("li", {"itemprop": "ingredient"})

        return [
            normalize_string(ingredient.get_text()) for ingredient in ingredients_html
        ]

    def instructions(self):
        instructions = self.soup.find("ul", {"itemprop": "instructions"}).findAll("li")

        instructions_arr = []
        for instruction in instructions:
            for tag in instruction.findAll("h2"):
                tag.replaceWith("")
            instructions_arr.append(normalize_string(instruction.get_text()))

        return "\n".join(instructions_arr)

    def yields(self):
        return get_yields(self.soup.find("span", {"class": "portion"}))
