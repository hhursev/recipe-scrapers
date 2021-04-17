from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class Yummly(AbstractScraper):
    @classmethod
    def host(cls):
        return "yummly.com"

    def title(self):
        found = self.soup.find("h1")
        return found.get_text() if found else None

    def total_time(self):
        data = self.soup.findAll("div", {"class": "recipe-summary-item"}, limit=2)
        return get_minutes(data[1]) if data else None

    def yields(self):
        return get_yields(self.soup.find("div", {"class": "servings"}))

    def ingredients(self):
        ingredients = self.soup.findAll("li", {"class": "IngredientLine"})

        return (
            [
                " ".join(
                    normalize_string(span.get_text())
                    for span in ingredient.select(
                        """
                        span[class^=amount],
                        span[class^=unit],
                        span[class^=ingredient],
                    span[class^=remainder]"""
                    )
                )
                for ingredient in ingredients
            ]
            if ingredients
            else None
        )

    def instructions(self):
        instructions = self.soup.findAll("li", attrs={"class": "prep-step"})
        return (
            "\n".join(normalize_string(instr.get_text()) for instr in instructions)
            if instructions
            else None
        )
