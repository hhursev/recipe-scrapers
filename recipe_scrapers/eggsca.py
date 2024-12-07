from ._abstract import AbstractScraper
from ._exceptions import StaticValueException
from ._grouping_utils import IngredientGroup


class EggsCa(AbstractScraper):
    @classmethod
    def host(cls):
        return "eggs.ca"

    def author(self):
        raise StaticValueException(return_value="Eggs.ca")

    def ingredients(self):
        return [
            " ".join(
                [
                    part.get_text(strip=True)
                    for part in ingredient.select(
                        ".ingredient__amount, .ingredient__ingredient"
                    )
                ]
            )
            for ingredient in self.soup.select(
                ".ingredients__sections .ingredient, .ingredients__wrap--simple .ingredient"
            )
        ]

    def ingredient_groups(self):
        all_ingredients = self.ingredients()
        sections = self.soup.select(".ingredients__sections .ingredients__section")
        if sections:
            grouped_ingredients = []
            for section in sections:
                section_ingredients = [
                    " ".join(
                        [
                            part.get_text(strip=True)
                            for part in ingredient.select(
                                ".ingredient__amount, .ingredient__ingredient"
                            )
                        ]
                    )
                    for ingredient in section.select(".ingredient")
                ]
                grouped_ingredients.append(
                    IngredientGroup(
                        ingredients=section_ingredients,
                        purpose=section.select_one(
                            ".ingredients__sectionHeading"
                        ).get_text(),
                    )
                )
            return grouped_ingredients
        else:
            return [IngredientGroup(ingredients=all_ingredients, purpose=None)]
