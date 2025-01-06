import re

from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_minutes, get_yields, normalize_string


class NHSHealthierFamilies(AbstractScraper):
    @classmethod
    def host(cls):
        return "nhs.uk"

    def author(self):
        return "NHS Better Health"

    def title(self):
        title = normalize_string(self.soup.find("h1").get_text())
        if title.endswith(" recipe"):
            title = title[:-7]
        return title

    def _get_recipe_content(self):
        container = self.soup.find("div", {"class": "bh-recipe__description"})
        descriptions = container.findAll("p")
        return "".join([description.get_text() for description in descriptions])

    def prep_time(self):
        content = self._get_recipe_content()
        prep_time = re.search(r"Prep: (\d+) mins", content)
        return get_minutes(prep_time.group(0)) if prep_time else 0

    def cook_time(self):
        content = self._get_recipe_content()
        cook_time = re.search(r"Cook: (\d+) mins", content)
        return get_minutes(cook_time.group(0)) if cook_time else 0

    def total_time(self):
        return self.prep_time() + self.cook_time()

    def yields(self):
        content = self._get_recipe_content()
        recipe_yields = re.search(r"Serves (\d+)", content)
        return get_yields(recipe_yields.group(0)) if recipe_yields else None

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".nhsuk-grid-column-one-third h3",
            ".nhsuk-grid-column-one-third li",
        )

    def instructions(self):
        instructions = (
            self.soup.find("div", {"class": "bh-recipe-instructions"})
            .find("ol")
            .findAll("li")
        )
        instructions = [
            instruction.find("p").get_text() for instruction in instructions
        ]
        return "\n".join(
            [normalize_string(instruction) for instruction in instructions]
        )
