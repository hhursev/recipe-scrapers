import re
from urllib.parse import urlparse

from ._abstract import AbstractScraper
from ._utils import FRACTIONS, get_minutes, normalize_string


class GrandFrais(AbstractScraper):
    @classmethod
    def host(cls):
        return "grandfrais.com"

    def category(self):
        return None

    def total_time(self):
        cook_time, prep_time = self.cook_time(), self.prep_time()
        if cook_time and prep_time:
            return cook_time + prep_time
        if prep_time:
            return prep_time
        return None

    def cook_time(self):
        raw = [
            item
            for item in self.soup.find_all("div", {"class": "pre-requie-item"})
            if "Cuisson" in item.text
        ]
        if raw:
            return get_minutes(raw[0].text)
        return None

    def prep_time(self):
        raw = [
            item
            for item in self.soup.find_all("div", {"class": "pre-requie-item"})
            if "Préparation" in item.text
        ]
        if raw:
            return get_minutes(raw[0].text)
        return None

    def image(self):
        img = self.soup.find("img", {"alt": self.title()})
        if img:
            canonical = urlparse(self.canonical_url())
            return f"{canonical.scheme}://{canonical.netloc}{img['src']}"
        return None

    def nutrients(self):
        return None

    def ingredients(self):
        ingredients = [
            self.__normalize_ingredient(i)
            for i in self.soup.find("div", {"itemprop": "ingredients"}).text.split("\n")
        ]

        for fraction, replacement in FRACTIONS.items():
            ingredients = [i.replace(fraction, str(replacement)) for i in ingredients]

        return ingredients

    def instructions(self):
        return "\n".join(
            [
                normalize_string(i.text)
                for i in self.soup.find(
                    "div", {"itemprop": "recipeInstructions"}
                ).find_all("ul")
            ]
        )

    def ratings(self):
        return None

    def author(self):
        return "Grand Frais"

    def cuisine(self):
        return None

    def description(self):
        return None

    def __normalize_ingredient(self, ingredient):
        """Normalize all ingredients to have a decimal point, remove the prepended dash, and remove any trailing whitespace."""
        return re.sub(
            r"^(\d+),(\d+)", r"\1.\2", normalize_string(ingredient.lstrip("-").strip())
        )
