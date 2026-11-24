import functools
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

        summary = self._get_summary
        if summary is None:
            return None

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
        recipe = self._get_recipe
        ingredients = recipe.find("div", {"class": "leftPanel"})

        if ingredients is None:
            ingredients = self._get_panel("Ingredients")

        return self._parse_list(ingredients)

    def ingredient_groups(self) -> list[IngredientGroup]:
        recipe = self._get_recipe
        ingredients = recipe.find("div", {"class": "leftPanel"})

        if ingredients is None:
            return [IngredientGroup(self.ingredients(), None)]

        groups = []

        headings = ingredients.find_all("h2")
        for heading in headings:
            ul = heading.find_next_sibling(name="ul")
            elements = self._parse_list(ul)
            ingredient_group = IngredientGroup(elements, heading.text)
            groups.append(ingredient_group)

        if not groups:
            return [IngredientGroup(self.ingredients(), None)]

        return groups

    def instructions(self):
        return "\n".join(self.instructions_list())

    def instructions_list(self) -> list[str]:
        recipe = self._get_recipe
        method = recipe.find("div", {"class": "rightPanel"})

        if method is None:
            method = self._get_panel("Method")

        return self._parse_list(method)

    @functools.cached_property
    def _get_recipe(self):
        """
        Get the recipe container element.
        """
        return self.soup.find("article") or self.soup

    @functools.cached_property
    def _get_summary(self):
        """
        Get the summary container element.
        """
        return self.soup.find("div", {"class": "blogRecipe-summary"})

    def _get_summary_value(self, field) -> str:
        """
        Get the value from the given summary field search string.
        """
        summary = self._get_summary

        if summary is None:
            return None

        item = summary.find("strong", string=field)
        return self._parse_summary_item(item)

    def _parse_summary_item(self, item):
        """
        Get the value associated with a summary field.
        """
        if item is None:
            return None

        value = item.find_next_sibling(name="p")
        return value.get_text(strip=True) if value else None

    def _get_panel(self, heading):
        """
        Find a recipe panel by its heading.
        """
        pattern = re.compile(
            rf"^\s*{re.escape(heading)}\s*:?\s*$",
            re.IGNORECASE,
        )

        for panel in self.soup.select("div.panel-text-two-columns"):
            if panel.find(["h2", "h3", "h4"], string=pattern):
                return panel

        return None

    def _parse_list(self, container) -> list[str]:
        if container is None:
            return []

        return [
            re.sub(r"\s+", " ", li.get_text()).strip()
            for li in container.find_all("li")
        ]
