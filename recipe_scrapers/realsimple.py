# mypy: disallow_untyped_defs=False
import re

from ._abstract import AbstractScraper
from ._utils import get_yields


class RealSimple(AbstractScraper):
    @classmethod
    def host(cls):
        return "realsimple.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        yield_container = self.soup.find("div", string=re.compile(r"Yield:"))
        if yield_container and yield_container.parent:
            return get_yields(yield_container.parent.get_text())

        return self.schema.yields()

    def ingredients(self):
        ingredient_elements = self.soup.findAll(
            "li", {"class": "mntl-structured-ingredients__list-item"}
        )
        extracted_ingredients = [
            element.get_text(strip=True, separator=" ")
            for element in ingredient_elements
            if element.get_text()
        ]

        if extracted_ingredients:
            return extracted_ingredients
        else:
            return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()
