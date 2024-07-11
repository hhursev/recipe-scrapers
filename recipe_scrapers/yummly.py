from ._abstract import AbstractScraper
from ._exceptions import StaticValueException
from ._utils import normalize_string


class Yummly(AbstractScraper):
    @classmethod
    def host(cls):
        return "yummly.com"

    def author(self):
        return self.soup.find("a", {"class": "markdown-link"}).get_text()

    def site_name(self):
        title = self.soup.find("title")
        if not title:
            raise StaticValueException(return_value="Yummly")
        _recipe, _delimiter, site_name = title.text.rpartition("|")
        return site_name.lstrip()

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
