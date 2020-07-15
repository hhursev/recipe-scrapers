from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class BudgetBytes(AbstractScraper):
    @classmethod
    def host(cls):
        return "budgetbytes.com"

    def title(self):
        return self.soup.find("h2", {"class": "wprm-recipe-name"}).get_text()

    def total_time(self):
        return get_minutes(
            self.soup.find("span", {"class": "wprm-recipe-total_time"}).parent
        )

    def yields(self):
        yields = self.soup.find("span", {"class": "wprm-recipe-servings"}).get_text()

        return get_yields("{} servings".format(yields))

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
        return round(
            float(
                self.soup.find(
                    "span", {"class": "wprm-recipe-rating-average"}
                ).get_text()
            ),
            2,
        )
