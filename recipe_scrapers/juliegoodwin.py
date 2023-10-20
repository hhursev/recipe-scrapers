# mypy: disallow_untyped_defs=False
import re

from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class JulieGoodwin(AbstractScraper):
    @classmethod
    def host(cls):
        return "juliegoodwin.com.au"

    def author(self):
        return "Julie Goodwin"

    def title(self):
        return normalize_string(self.soup.find("h1").get_text())

    def total_time(self):
        mins = 0
        prep = self.soup.find(string=re.compile("Prep time"))
        if prep:
            prep_hours_match = re.search(r"(\d+) hours", prep.parent.parent.get_text())
            if prep_hours_match:
                mins += 60 * int(prep_hours_match.group(1))
            prep_mins_match = re.search(r"(\d+) mins", prep.parent.parent.get_text())
            if prep_mins_match:
                mins += int(prep_mins_match.group(1))

        cooking = self.soup.find(string=re.compile("Cooking time"))
        if cooking:
            cooking_hours_match = re.search(
                r"(\d+) hours", cooking.parent.parent.get_text()
            )
            if cooking_hours_match:
                mins += 60 * int(cooking_hours_match.group(1))
            cooking_mins_match = re.search(
                r"(\d+) mins", cooking.parent.parent.get_text()
            )
            if cooking_mins_match:
                mins += int(cooking_mins_match.group(1))

        return get_minutes(mins)

    def yields(self):
        return normalize_string(self.soup.find("h4").get_text())

    def image(self):
        container = self.soup.find("div", {"class": "inner-wrap"})
        if not container:
            return None

        image = container.find("img", {"src": True})
        return image["src"] if image else None

    def ingredients(self):
        ingredients = self.soup.find("ul", {"class", "ingredients"}).findAll("li")
        if ingredients:
            return [
                normalize_string(ingredient.get_text()) for ingredient in ingredients
            ]

        heading = self.soup.find(string="Ingredients")
        ingredients = heading.parent.next
        if ingredients:
            pass

    def instructions(self):
        instructions = self.soup.findAll(string=re.compile("STEP "))
        return "\n".join(
            [
                normalize_string(inst.parent.parent.get_text().split("|")[1])
                for inst in instructions
            ]
        )
