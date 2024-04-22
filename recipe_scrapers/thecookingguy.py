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

        # find all ingredient group purposes
        ingredient_group_ps = ingredients_div.find_all("p")
        ingredient_group_ps = [
            p for p in ingredient_group_ps if p.findChildren("strong")
        ]

        # find all ingredient lists
        ungrouped_ingredient_uls = ingredients_div.find_all("ul")

        # create ingredient groups associated with those purposes
        # skips ungrouped ingredients
        ingredient_groups = []
        for ingredient_group_p in ingredient_group_ps:
            ingredients_ul = ingredient_group_p.find_next_sibling()
            ungrouped_ingredient_uls.remove(
                ingredients_ul
            )  # remove list from ungrouped

            ingredients = ingredients_ul.find_all("li")
            items = [
                normalize_string(ingredient.get_text()) for ingredient in ingredients
            ]
            group = IngredientGroup(
                ingredients=items,
                purpose=normalize_string(ingredient_group_p.find("strong").get_text()),
            )
            ingredient_groups.append(group)

        # now group ungrouped items into null purpose
        if len(ungrouped_ingredient_uls) > 0:
            items = []

            for ul in ungrouped_ingredient_uls:
                ingredients = ul.find_all("li")
                items.extend(
                    [
                        normalize_string(ingredient.get_text())
                        for ingredient in ingredients
                    ]
                )

            group = IngredientGroup(
                ingredients=items,
                purpose=None,
            )
            ingredient_groups.append(group)

        return ingredient_groups

    def instructions(self):
        if (
            self.soup.find(
                "div", class_="w-layout-vflex card-text-holder directions"
            ).find_all("p")
            is None
        ):

            instructions = self.soup.find(
                "div", class_="w-layout-vflex card-text-holder directions"
            ).find_all("li")

            instructions_text = "\n".join(
                normalize_string(instruction.get_text()) for instruction in instructions
            )

            return instructions_text
        else:
            headings = self.soup.find(
                "div", class_="w-layout-vflex card-text-holder directions"
            ).find_all("p")

            headings = [heading for heading in headings if heading.find("strong")]

            output = []
            for heading in headings:
                if heading.find_next_sibling() is None:
                    continue
                heading_text = normalize_string(heading.get_text())
                list_items = heading.find_next_sibling().find_all("li")
                list_items_text = "\n".join(
                    normalize_string(item.get_text()) for item in list_items
                )
                heading_text += "\n" + list_items_text
                output.append(heading_text)

            return "\n".join(output)

    def description(self):
        return self.schema.description()
