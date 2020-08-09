from ._abstract import AbstractScraper
from ._utils import normalize_string, get_yields


class BonAppetit(AbstractScraper):
    @classmethod
    def host(cls):
        return "bonappetit.com"

    def title(self):
        return self.soup.find("h1", {"itemprop": "name"}).get_text()

    def total_time(self):
        return 0

    def yields(self):
        return get_yields(
            self.soup.find(
                "span",
                {
                    "class": "recipe__header__servings recipe__header__servings--basically"
                },
            ).find("span")
        )

    def ingredients(self):
        ingredients = self.soup.findAll("li", {"class": "ingredient"})

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = [txt.findAll("li") for txt in scraper.soup.find_all("div", {"class": "steps-wrapper"})]
        instructions = [item for sublist in instructions for item in sublist]

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
