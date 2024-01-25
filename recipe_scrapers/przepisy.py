# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._utils import get_yields, normalize_string


class Przepisy(AbstractScraper):
    @classmethod
    def host(cls):
        return "przepisy.pl"

    def title(self):
        return self.schema.title()

    def author(self):
        return self.schema.author()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return get_yields(self.soup.find("div", {"class": "person-count"}))

    def ingredients(self):
        ingredients = self.soup.findAll("span", {"class": "text-bg-white"})

        return [
            normalize_string(i.get_text()) + " " + normalize_string(j.get_text())
            for i, j in zip(ingredients[0::2], ingredients[1::2])
        ]

    def instructions(self):
        return self.schema.instructions()
