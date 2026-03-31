from itertools import chain
from urllib.parse import urljoin

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields
from ._grouping_utils import group_ingredients, IngredientGroup


class GrimGrains(AbstractScraper):
    @classmethod
    def host(cls):
        return "grimgrains.com"

    def author(self):
        return "Hundred Rabbits"

    def title(self):
        return self.soup.main.h1.string

    def total_time(self):
        return get_minutes(self.soup.main.h2.string.split("—")[1])

    def yields(self):
        return get_yields(self.soup.main.h2.string.split("—")[0])

    def image(self):
        return urljoin(self.url, self.soup.main.find("img")["src"])

    def ingredients(self):
        return [
            f"{i.b.text}: {i.u.text}"
            for i in chain.from_iterable(self.soup.main("dl", "ingredients"))
            if i.b
        ]

    def ingredient_groups(self):
        headings = self.soup.select("dl.ingredients h3")
        if len(headings) <= 1:
            return [IngredientGroup(ingredients=self.ingredients())]
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "dl.ingredients h3",
            "dl.ingredients dt",
        )

    def instructions(self):
        instructions = [i("li") for i in self.soup.main("ul", "instructions")]
        return "\n".join([i.text for i in chain.from_iterable(instructions)])
