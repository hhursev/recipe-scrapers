from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml, FieldNotProvidedByWebsiteException
from ._grouping_utils import IngredientGroup
from ._utils import get_yields, normalize_string


class TheCookingGuy(AbstractScraper):
    @classmethod
    def host(cls):
        return "thecookingguy.com"

    def total_time(self):
        raise FieldNotProvidedByWebsiteException(return_value=None)

    def yields(self):
        return get_yields(self.soup.find("div", class_="text-block-7").get_text())

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

        # initialize ingredient groups
        ingredient_groups = []
        ungrouped_ingredients = []

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
                ungrouped_ingredients.extend(items)

        if ungrouped_ingredients:
            group = IngredientGroup(ingredients=ungrouped_ingredients, purpose=None)
            ingredient_groups.append(group)

        return ingredient_groups

    def instructions(self):
        instructions_div = self.soup.find(
            "div", class_="w-layout-vflex card-text-holder directions"
        ).find("div")

        instructions = []
        for child in instructions_div.children:
            if child.name == "p":
                heading = child.find("strong")
                if heading and heading.get_text().encode("ascii", "ignore").strip():
                    instructions.append(normalize_string(heading.get_text()))
            elif child.name == "ol":
                instructions.extend(
                    normalize_string(instruction.get_text())
                    for instruction in child.find_all("li")
                )

        return "\n".join(instructions)

    def description(self):
        description = self.soup.find("div", class_="richintro w-richtext").find("p")
        description_text = normalize_string(description.get_text())
        return description_text

    def site_name(self):
        return "Sam The Cooking Guy"
