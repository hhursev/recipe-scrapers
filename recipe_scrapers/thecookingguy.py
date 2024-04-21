# mypy: allow-untyped-defs
from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml
from ._grouping_utils import IngredientGroup
from ._utils import get_yields, normalize_string


class TheCookingGuy(AbstractScraper):
    @classmethod
    def host(cls):
        return "thecookingguy.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def total_time(self):
        return None

    def yields(self):
        return get_yields(self.soup.find("div", class_="text-block-7").get_text())

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredients = self.soup.find(
            "div", class_="w-layout-vflex card-text-holder ingredients"
        ).find_all("li")
        ingredients_text = [
            normalize_string(ingredient.get_text()) for ingredient in ingredients
        ]
        return ingredients_text

    def ingredient_groups(self):
        # find ingredients div
        ingredients_div = self.soup.find(
            "div", class_="w-layout-vflex card-text-holder ingredients"
        )

        if ingredients_div is None:
            raise ElementNotFoundInHtml("Ingredients not found.")

        # initialize ingredient groups with 0th group being ungrouped
        ingredient_groups = []
        group = IngredientGroup(
            ingredients=[],
            purpose=None,
        )
        ingredient_groups.append(group)

        for ingredients_ul in ingredients_div.find_all("ul"):
            ingredients = ingredients_ul.find_all("li")
            items = [
                normalize_string(ingredient.get_text()) for ingredient in ingredients
            ]

            purpose_p = ingredients_ul.find_previous_sibling()

            if purpose_p and purpose_p.name == "p" and purpose_p.find("strong"):
                # has purpose, add new group
                group = IngredientGroup(
                    ingredients=items,
                    purpose=normalize_string(purpose_p.find("strong").get_text()),
                )
                ingredient_groups.append(group)
            else:
                # no purpose, add to no purpose group
                ingredient_groups[0].ingredients.extend(items)

        return ingredient_groups

    def instructions(self):
        instructions = self.soup.find(
            "div", class_="w-layout-vflex card-text-holder directions"
        ).find_all("li")

        instructions_text = "\n".join(
            normalize_string(instruction.get_text()) for instruction in instructions
        )

        return instructions_text

    def description(self):
        return self.schema.description()
