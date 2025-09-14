from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class OhSweetBasil(AbstractScraper):
    @classmethod
    def host(cls):
        return "ohsweetbasil.com"

    def ingredients(self):
        return [
            " ".join(
                span.get_text(strip=True)
                for span in ingredient.select(
                    ".wprm-recipe-ingredient-amount, "
                    ".wprm-recipe-ingredient-unit, "
                    ".wprm-recipe-ingredient-name, "
                    ".wprm-recipe-ingredient-notes"
                )
                if span.get_text(strip=True)
            ).strip()
            for ingredient in self.soup.select(
                ".wprm-recipe-ingredient-group li.wprm-recipe-ingredient"
            )
            if ingredient.select_one(".wprm-recipe-ingredient-name")
        ]

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient-group li.wprm-recipe-ingredient:has(.wprm-recipe-ingredient-name)",
        )
