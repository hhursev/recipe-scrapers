from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import normalize_string


class UitPaulinesKeukenNL(AbstractScraper):
    @classmethod
    def host(cls):
        return "uitpaulineskeuken.nl"

    def ingredients(self):
        ingredients = self.soup.find("section", {"id": "ingredienten"}).findChildren(
            "li"
        )
        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "#ingredienten > h2",
            "#ingredienten > ul > li",
        )

    def instructions(self):
        instructions = self.soup.find(
            "div", {"class": "preparation-list"}
        ).findChildren("p")
        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    def description(self):
        return normalize_string(
            self.soup.find("article", {"class": "single-recipe"})
            .findChild("section", {"class": "text"})
            .find_next()
            .get_text()
        )
