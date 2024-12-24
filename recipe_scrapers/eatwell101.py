import html
import re

from ._abstract import AbstractScraper
from ._utils import normalize_string


class EatWell101(AbstractScraper):
    @classmethod
    def host(cls):
        return "eatwell101.com"

    def category(self):
        return html.unescape(self.schema.category())

    def ingredients(self):
        ingredients_h2 = self.soup.find(
            "h2", string=re.compile(r"Ingredients", re.IGNORECASE)
        )
        ingredients_ul = ingredients_h2.find_next("ul")
        ingredients_list = [item.text.strip() for item in ingredients_ul.find_all("li")]
        normalized_ingredients = [
            normalize_string(ingredient) for ingredient in ingredients_list
        ]

        return normalized_ingredients

    def instructions(self):
        directions_h2 = self.soup.find("h2", string="Directions")
        instructions_list = []
        if directions_h2:
            next_sibling = directions_h2.find_next_sibling()
            while next_sibling:
                if next_sibling.name == "p" and next_sibling.find("strong"):
                    instruction_text = normalize_string(next_sibling.text.strip())
                    instructions_list.append(instruction_text)
                    next_sibling = next_sibling.find_next_sibling()
                else:
                    break

        return "\n".join(instructions_list)

    def description(self):
        return self.soup.find("div", {"class": "saveurteaser"}).get_text()
