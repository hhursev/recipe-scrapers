# mypy: allow-untyped-defs

import re
from itertools import zip_longest

from recipe_scrapers._grouping_utils import IngredientGroup

from ._abstract import AbstractScraper
from ._utils import normalize_string


class KuchynaLidla(AbstractScraper):
    @classmethod
    def host(cls):
        return "kuchynalidla.sk"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category().strip()

    def total_time(self):
        return self.schema.total_time()

    def cook_time(self):
        return self.schema.cook_time()

    def prep_time(self):
        return self.schema.prep_time()

    def yields(self):
        yields = self.schema.yields()
        yields = yields.replace("servings", "porcií")
        yields = yields.replace("serving", "porcia")
        return yields

    def image(self):
        return self.schema.image()

    def ingredient_groups(self):
        raw_groups = (
            self.schema.data.get("recipeIngredient")
            or self.data.get("raw_groups")
            or []
        )

        raw_groups = "".join(raw_groups)
        raw_groups = raw_groups.replace("<br>", "")

        # split on atleast two newlines
        raw_groups = re.split(r"[\n\r]{3,10}", raw_groups)
        raw_groups = [i for i in raw_groups if normalize_string(i)]
        if len(raw_groups) == 1:
            return IngredientGroup(ingredients=raw_groups[0].splitlines())

        # we have one general heading that has no ingredients,
        # the other headings are respective group headings
        if len(raw_groups) % 2 == 1:
            raw_groups.pop(0)

        def grouper(iterable, n, fillvalue=None):
            "Collect data into fixed-length chunks or blocks"
            # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
            args = [iter(iterable)] * n
            return zip_longest(*args, fillvalue=fillvalue)

        groups = []
        for purpose, group in grouper(raw_groups, 2):
            ingredients = [
                norm for i in group.splitlines() if (norm := normalize_string(i))
            ]
            groups.append(IngredientGroup(ingredients=ingredients, purpose=purpose))

        return groups

    def ingredients(self):
        return [i for ig in self.ingredient_groups() for i in ig.ingredients]

    def instructions(self):
        return self.schema.instructions()

    def instructions_list(self):
        il = re.split(r"[\n\r]{3,10}", self.instructions())
        il = [norm for i in il if (norm := normalize_string(i))]
        return il

    def ratings(self):
        return self.schema.ratings()

    def description(self):
        return self.schema.description()

    def language(self):
        return "sk"
