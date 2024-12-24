import re

from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import normalize_string


class GoodHousekeeping(AbstractScraper):
    @classmethod
    def host(cls):
        return "goodhousekeeping.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".ingredients-body h3",
            ".ingredient-lists li",
        )

    def instructions(self):
        directions = self.soup.find(
            "ul",
            class_="directions",
        )

        methods = [
            directions.find_all("p"),
            directions.find("li", recursive=False).find_all("li"),
        ]

        for m in methods:
            if len(m) != 0:
                instructions = m
                break

        return "\n".join(
            [
                re.sub(
                    r"Step \d+", "", normalize_string(instruction.get_text())
                ).strip()
                for instruction in instructions
            ]
        )

    def cuisine(self):
        return self.schema.cuisine() or None

    def _find_nutrient(self, prefix):
        nutrient = self.nutrient_soup.find(string=re.compile(prefix))
        if nutrient is not None:
            return re.sub(prefix, "", nutrient, count=1).lstrip(":").strip()
        else:
            return None

    def nutrients(self):
        self.nutrient_soup = self.soup.find(class_="recipe-body-content")
        nutrients = {
            "calories": self._find_nutrient("Calories"),
            "fatContent": self._find_nutrient("(Total )?[Ff]at"),
            "saturatedFatContent": self._find_nutrient("(Saturates|Sat(urated)? fat)"),
            "sugarContent": self._find_nutrient("(Total )?[Ss]ugars"),
            "carbohydrateContent": self._find_nutrient("(Total )?[Cc]arbs"),
            "proteinContent": self._find_nutrient("Protein"),
            "fiberContent": self._find_nutrient("Fib(er|re)"),
        }
        return {
            nutrient: quantity
            for nutrient, quantity in nutrients.items()
            if quantity is not None
        }
