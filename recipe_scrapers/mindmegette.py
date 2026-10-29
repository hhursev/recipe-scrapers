import re

from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup, group_ingredients

GROUP_HEADING = ".ingredients-wrapper .ingredients-group"
GROUP_ELEMENT = ".ingredients-wrapper .ingredients-meta"


class Mindmegette(AbstractScraper):
    @classmethod
    def host(cls):
        return "mindmegette.hu"

    def title(self):
        # the site name is sometimes repeated
        return re.sub(r"(\s*\|\s*Mindmegette\.hu)+$", "", self.schema.title())

    def ingredient_groups(self):
        ingredients = self.ingredients()
        if not self.soup.select(GROUP_HEADING):
            return [IngredientGroup(ingredients=ingredients)]

        # page text is lowercase but the schema's isn't, so match lowercased
        # and map back by position
        lowered = [i.lower() for i in ingredients]
        groups = group_ingredients(lowered, self.soup, GROUP_HEADING, GROUP_ELEMENT)
        unused = list(range(len(ingredients)))
        for group in groups:
            for n, item in enumerate(group.ingredients):
                i = next((i for i in unused if lowered[i] == item), lowered.index(item))
                if i in unused:
                    unused.remove(i)
                group.ingredients[n] = ingredients[i]
        return groups

    def instructions(self):
        # step names are just "1. lépés" (step 1), "2. lépés" etc.
        return "\n".join(
            line
            for line in self.schema.instructions().split("\n")
            if not re.fullmatch(r"\d+\.\s*lépés", line, re.IGNORECASE)
        )
