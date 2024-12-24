import re

from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup
from ._utils import get_minutes


class KitchenAidAustralia(AbstractScraper):
    @classmethod
    def host(cls):
        return "kitchenaid.com.au"

    def total_time(self):
        time_pattern = re.compile("time", re.IGNORECASE)

        summary = self._get_summary()
        time_items = summary.find_all("strong", string=time_pattern)

        if not time_items:
            return None

        # The last item is always the total time
        time_item = time_items[-1]
        total_time = self._parse_summary_item(time_item)

        return get_minutes(total_time)

    def yields(self):
        return self._get_summary_value("Makes")

    def ingredients(self):
        recipe = self._get_recipe()
        ingredients = recipe.find("div", {"class": "leftPanel"})

        elements = self._parse_list(ingredients)
        return elements

    def ingredient_groups(self) -> list[IngredientGroup]:
        recipe = self._get_recipe()
        ingredients = recipe.find("div", {"class": "leftPanel"})

        groups = []

        headings = ingredients.find_all("h2")
        for heading in headings:
            ul = heading.find_next_sibling("ul")
            elements = self._parse_list(ul)
            ingredient_group = IngredientGroup(elements, heading.text)
            groups.append(ingredient_group)

        return groups

    def instructions(self):
        return "\n".join(self.instructions_list())

    def instructions_list(self) -> list[str]:
        recipe = self._get_recipe()
        method = recipe.find("div", {"class": "rightPanel"})

        return self._parse_list(method)

    def _get_recipe(self):
        """
        Get the recipe container element.
        """
        return self.soup.find("article")

    def _get_summary(self):
        """
        Get the summary container element.
        """
        return self.soup.find("div", {"class": "blogRecipe-summary"})

    def _get_summary_value(self, field) -> str:
        """
        Get the value from the given summary field search string.
        """
        summary = self._get_summary()

        item = summary.find("strong", string=field)
        return self._parse_summary_item(item)

    def _parse_summary_item(self, item):
        """
        Get the value associated with a summary field.
        """
        return item.find_next_sibling("p").text

    def _parse_list(self, container) -> list[str]:
        """
        Get the text from each of the li elements contained by the given container.
        """
        li_list = container.find_all("li")

        elements = [li.text for li in li_list]

        return elements
