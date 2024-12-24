import re

from bs4 import BeautifulSoup

from ._abstract import AbstractScraper
from ._utils import get_yields, normalize_string


class MyKitchen101(AbstractScraper):
    @classmethod
    def host(cls):
        return "mykitchen101.com"

    def author(self):
        return self.soup.find("a", {"rel": "author"}).get_text()

    def title(self):
        return self.soup.find("h1", {"class": "entry-title"}).get_text()

    def yields(self):
        return get_yields(self.soup.find("p", string=re.compile("分量：")).get_text())

    def ingredients(self):
        soup = BeautifulSoup(str(self.soup), features="html.parser")
        ingredients = (
            soup.find(name="p", string=re.compile("材料："))
            .find_next("ul")
            .find_all("li")
        )
        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        soup = BeautifulSoup(str(self.soup), features="html.parser")
        instructions = soup.find(name="p", string=re.compile("做法：")).find_all_next(
            "p"
        )
        return "\n".join(
            [
                normalize_string(instruction.get_text())
                for instruction in instructions
                if instruction.get_text()[:1].isdigit()
            ]
        )

    def equipment(self):
        return list(
            {
                normalize_string("".join(item.stripped_strings).split("(")[0].strip())
                for item in self.soup.find_all(
                    "div", class_="wprm-recipe-equipment-name"
                )
            }
        )
