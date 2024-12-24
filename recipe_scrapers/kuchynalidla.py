import re
from itertools import zip_longest

from recipe_scrapers._grouping_utils import IngredientGroup

from ._abstract import AbstractScraper
from ._utils import normalize_string


class KuchynaLidla(AbstractScraper):
    @classmethod
    def host(cls):
        return "kuchynalidla.sk"

    def category(self):
        return self.schema.category().strip()

    def yields(self):
        yields = self.schema.yields()
        yields = yields.replace("servings", "porcií")
        yields = yields.replace("serving", "porcia")
        return yields

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

    def instructions_list(self):
        il = re.split(r"[\n\r]{3,10}", self.instructions())
        il = [norm for i in il if (norm := normalize_string(i))]
        return il

    def language(self):
        return super().language()
