from ._abstract import AbstractScraper
from ._exceptions import StaticValueException
from ._utils import normalize_string


class TastyKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "tastykitchen.com"

    def title(self):
        return self.soup.find("h1", {"itemprop": "name"}).get_text()

    def site_name(self):
        current_selection = next(
            iter(self.soup.select("div.tpw-network a.selected")), None
        )
        if not current_selection:
            raise StaticValueException(return_value="Tasty Kitchen")
        return current_selection.text

    def ingredients(self):
        ingredients = self.soup.find("ul", {"class": "ingredients"}).findAll("li")

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = self.soup.find("span", {"itemprop": "instructions"}).findAll("p")

        return "\n".join(
            [normalize_string(direction.get_text()) for direction in instructions]
        )
