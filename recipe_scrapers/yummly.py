from ._abstract import AbstractScraper
from ._utils import normalize_string, get_yields


class Yummly(AbstractScraper):
    @classmethod
    def host(cls):
        return "yummly.com"

    def title(self):
        return self.soup.find("h1").get_text()

    def total_time(self):
        return int(
            self.soup.findAll("div", {"class": "recipe-summary-item"})[1].span.text
        )

    def yields(self):
        return get_yields(self.soup.find("div", {"class": "servings"}).span.text)

    def ingredients(self):
        ingredients = self.soup.findAll("li", {"class": "IngredientLine"})

        return [
            " ".join(
                [
                    normalize_string(span.get_text())
                    for span in ingredient.select(
                        """
                    span[class^=amount],
                    span[class^=unit],
                    span[class^=ingredient],
                    span[class^=remainder]"""
                    )
                ]
            )
            for ingredient in ingredients
        ]

    def instructions(self):
        instructions = self.soup.findAll("li", attrs={"class": "prep-step"})
        return (
            "\n".join([normalize_string(instr.get_text()) for instr in instructions])
            if instructions is not None
            else ""
        )
