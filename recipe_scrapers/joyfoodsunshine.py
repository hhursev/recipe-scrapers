from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class Joyfoodsunshine(AbstractScraper):
    @classmethod
    def host(cls):
        return "joyfoodsunshine.com"

    def author(self):
        return self.soup.find("span", {"class": "entry-author-name"}).get_text()

    def title(self):
        return self.soup.find("h2", {"class": "wprm-recipe-name"}).get_text()

    def total_time(self):
        return get_minutes(
            self.soup.find("span", {"class": "wprm-recipe-total_time-minutes"}).text
        )

    def yields(self):
        return get_yields(
            normalize_string(
                self.soup.find("span", {"class": "wprm-recipe-servings"}).text
            )
        )

        return self.schema.ingredients()

    def image(self):
        # span class = wprm-recipe-image find src
        return self.schema.image()

    def ingredients(self):
        ingredients = self.soup.findAll("li", {"class": "wprm-recipe-ingredient"})

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = self.soup.findAll(
            "div", {"class": "wprm-recipe-instruction-text"}
        )

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    def ratings(self):
        data = self.soup.find("span", {"class": "wprm-recipe-rating-average"})
        return round(float(data.get_text()), 2) if data else None
