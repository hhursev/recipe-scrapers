from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class HEB(AbstractScraper):
    @classmethod
    def host(self, domain="com"):
        return f"www.heb.{domain}"

    def title(self):
        return self.soup.find("h1", {"class": "title"}).get_text()

    def total_time(self):
        minutes_tag = self.soup.find("div", {"itemprop": "totalTime"})
        return get_minutes(minutes_tag.parent.get_text())

    def yields(self):
        yields_tag = self.soup.find("div", {"itemprop": "recipeYield"})
        return get_yields(yields_tag.parent.get_text())

    def ingredients(self):
        ingredients_container = self.soup.find(class_="ingredientswrapper")
        ingredients = ingredients_container.findAll("div", {"class": "recipestepstxt"})

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def _instructions_list(self):
        instructions_container = self.soup.find("div", {"class": "instructions"})
        instructions = instructions_container.findAll(
            "span", {"class": "instructiontxt"}
        )
        return [
            normalize_string(instruction.get_text()) for instruction in instructions
        ]

    def instructions(self):
        data = self._instructions_list()
        return "\n".join(data) if data else None

    def image(self):
        container = self.soup.find("div", {"class": "recipeimage"})
        if not container:
            return None

        image = container.find("img", {"src": True})
        return image["src"] if image else None
