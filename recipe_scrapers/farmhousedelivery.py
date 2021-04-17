import re

from bs4 import Tag

from ._abstract import AbstractScraper
from ._utils import normalize_string

"""
    NOTE: This website has at least 2 prominent layouts styles, so there are two logic blocks and 2 test cases to
    support in ingredients and instructions processing sections.
"""


class FarmhouseDelivery(AbstractScraper):
    @classmethod
    def host(self, domain="com"):
        return f"recipes.farmhousedelivery.{domain}"

    def title(self):
        return self.soup.find("h1", {"class": "entry-title"}).get_text(strip=True)

    def ingredients(self):
        # Style 1
        ingredients_marker = self.soup.find("p", text=re.compile(r"Ingredients:"))
        if ingredients_marker is not None:
            ingredients_marker_siblings = ingredients_marker.next_siblings
            for ingredients_marker_sibling in ingredients_marker_siblings:
                if (
                    isinstance(ingredients_marker_sibling, Tag)
                    and ingredients_marker_sibling.name == "ul"
                ):
                    ingredients = ingredients_marker_sibling.findAll("li")
                    return [
                        normalize_string(ingredient.get_text())
                        for ingredient in ingredients
                    ]

        # Style 2
        ingredients_marker = self.soup.find("p", text=re.compile(r"Ingredients"))
        if ingredients_marker is not None:
            ingredients = []
            ingredients_marker_siblings = ingredients_marker.next_siblings
            for ingredients_marker_sibling in ingredients_marker_siblings:
                if (
                    isinstance(ingredients_marker_sibling, Tag)
                    and ingredients_marker_sibling.name == "p"
                ):
                    if ingredients_marker_sibling.get_text() == "Instructions":
                        break
                    else:
                        ingredients.append(
                            normalize_string(ingredients_marker_sibling.get_text())
                        )
            return ingredients

        return None

    def _instructions_list(self):
        # Style 1
        instructions_marker = self.soup.find("p", text=re.compile(r"Instructions:"))
        if instructions_marker is not None:
            instructions_marker_siblings = instructions_marker.next_siblings
            for instructions_marker_sibling in instructions_marker_siblings:
                if (
                    isinstance(instructions_marker_sibling, Tag)
                    and instructions_marker_sibling.name == "p"
                    and instructions_marker_sibling.get_text(strip=True) != ""
                ):
                    instructions = instructions_marker_sibling.findAll("span")
                    return [
                        normalize_string(instruction.get_text())
                        for instruction in instructions
                    ]

        # Style 2
        instructions_marker = self.soup.find("p", text=re.compile(r"Instructions"))
        if instructions_marker is not None:
            instructions = []
            instructions_marker_siblings = instructions_marker.next_siblings
            for instructions_marker_sibling in instructions_marker_siblings:
                if (
                    isinstance(instructions_marker_sibling, Tag)
                    and instructions_marker_sibling.name == "p"
                    and instructions_marker_sibling.get_text(strip=True) != ""
                ):
                    instructions.append(
                        normalize_string(instructions_marker_sibling.get_text())
                    )
            return instructions

        return None

    def instructions(self):
        data = self._instructions_list()
        return "\n".join(data) if data else None

    def image(self):
        container = self.soup.find("div", {"class": "entry-content"})
        if not container:
            return None

        image = container.find("img", {"src": True})
        return image["src"] if image else None
