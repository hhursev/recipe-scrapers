# mypy: allow-untyped-defs

import re
from typing import List

from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup
from ._utils import get_minutes


class KitchenAidAustralia(AbstractScraper):
    @classmethod
    def host(cls):
        return "kitchenaid.com.au"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        time_pattern = re.compile("time", re.IGNORECASE)

        summary = self.get_summary()
        time_items = summary.find_all("strong", string=time_pattern)

        if not time_items:
            return None

        # The last item is always the total time
        time_item = time_items[-1]
        total_time = self.parse_summary_item(time_item)

        return get_minutes(total_time)

    def yields(self):
        return self.get_summary_value("Makes")

    def image(self):
        return self.schema.image()

    def ingredients(self):
        recipe = self.get_recipe()
        ingredients = recipe.find("div", {"class": "leftPanel"})

        elements = self.parse_list(ingredients)
        return elements

    def ingredient_groups(self) -> List[IngredientGroup]:
        recipe = self.get_recipe()
        ingredients = recipe.find("div", {"class": "leftPanel"})

        groups = []

        headings = ingredients.find_all("h2")
        for heading in headings:
            ul = heading.find_next_sibling("ul")
            elements = self.parse_list(ul)
            ingredient_group = IngredientGroup(elements, heading.text)
            groups.append(ingredient_group)

        return groups

    def instructions(self):
        return "\n".join(self.instructions_list())

    def instructions_list(self) -> List[str]:
        recipe = self.get_recipe()
        method = recipe.find("div", {"class": "rightPanel"})

        return self.parse_list(method)

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()

    def get_recipe(self):
        """
        Get the recipe container element.
        """
        return self.soup.find("article")

    def get_summary(self):
        """
        Get the summary container element.
        """
        return self.soup.find("div", {"class": "blogRecipe-summary"})

    def get_summary_value(self, field) -> str:
        """
        Get the value from the given summary field search string.
        """
        summary = self.get_summary()

        item = summary.find("strong", string=field)
        return self.parse_summary_item(item)

    def parse_summary_item(self, item):
        """
        Get the value associated with a summary field.
        """
        return item.find_next_sibling("p").get_text()

    def parse_list(self, container) -> List[str]:
        """
        Get the text from each of the li elements contained by the given container.
        """
        li_list = container.find_all("li")

        elements = [li.get_text() for li in li_list]

        return elements
