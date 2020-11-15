from ._abstract import AbstractScraper
from ._utils import normalize_string


class HeinzBrasil(AbstractScraper):
    @classmethod
    def host(cls):
        return "heinzbrasil.com.br"

    def title(self):
        return self.soup.find("h1", {"class": "krRDPrecName"}).get_text()

    def total_time(self):
        return 0

    def image(self):
        return self.soup.find("img", {"class": "krBanImg"})["src"]

    def ingredients(self):
        ingredients = self.soup.findAll("div", {"class": "krRDPIngreListText"})

        return [
            normalize_string(
                "{} {}".format(ingredient["qty"], ingredient["ingredientname"])
            )
            for ingredient in ingredients
        ]

    def instructions(self):
        instructions = (
            self.soup.find("div", {"class": "krRecipeMakeItText"})
            .findNext("div", {"class": "class"})
            .nextSibling
        )
        return normalize_string(instructions.get_text())
