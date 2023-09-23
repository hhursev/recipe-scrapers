# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._utils import normalize_string


class Waitrose(AbstractScraper):
    @classmethod
    def host(cls):
        return "waitrose.com"

    def author(self):
        return "waitrose.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        img_tag = self.soup.find("img", {"itemprop": "image"})
        if img_tag:
            url = img_tag.get("src")
            return url[2:] if url.startswith("//") else url

    def ingredients(self):
        ingredients_div = self.soup.find("div", {"class": "ingredients"})

        if ingredients_div:
            ingredient_items = ingredients_div.find_all("li")
            ingredient_text = [
                normalize_string(item.get_text())
                for item in ingredient_items
                if item.get_text()
            ]
            return ingredient_text

    def extract_instructions(self):
        instructions_div = self.soup.find("div", {"class": "ingredients"})

        if instructions_div:
            instruction_items = instructions_div.find_all("li")
            instruction_text = [
                normalize_string(item.get_text())
                for item in instruction_items
                if item.get_text()
            ]
            return "\n".join(instruction_text)

    def ratings(self):
        return self.schema.ratings()

    def description(self):
        return self.schema.description()
