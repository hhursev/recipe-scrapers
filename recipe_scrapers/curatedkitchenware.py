import json
import re

from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup
from ._utils import normalize_string


class CuratedKitchenware(AbstractScraper):
    """Scraper for curatedkitchenware.com (Shopify, RecipeKit app).

    RecipeKit renders this site's ingredient/direction group headings
    client-side via JS — the static HTML's own group markers
    (``h3.rk_group_heading``) carry no real text at all, just the literal
    placeholder "blank". The real heading text only exists in a separate
    ``<script type="application/json" id="recipe-data-*">`` block RecipeKit
    ships for its own editor, alongside every ingredient/direction in
    document order, each entry typed ``heading``/``ingredient``/
    ``direction``. That JSON is the only reliable source for groups on
    this site; schema.org's ``recipeIngredient``/``recipeInstructions``
    are flat and lose all of it, same as the group markers do.
    """

    @classmethod
    def host(cls):
        return "curatedkitchenware.com"

    def _recipe_data(self):
        if getattr(self, "_recipe_data_cache", None) is not None:
            return self._recipe_data_cache
        match = re.search(
            r'<script type="application/json" id="recipe-data-\d+">(.*?)</script>',
            self.page_data,
            re.S,
        )
        data = json.loads(match.group(1)) if match else {}
        self._recipe_data_cache = data
        return data

    def ingredient_groups(self):
        groups = []
        current_purpose = None
        current_ingredients = []
        for item in self._recipe_data().get("recipe_ingredients", []):
            if item.get("type") == "heading":
                if current_ingredients:
                    groups.append(IngredientGroup(current_ingredients, current_purpose))
                current_purpose = normalize_string(item.get("heading_text", "")) or None
                current_ingredients = []
            else:
                text = normalize_string(item.get("ingredient", ""))
                if text:
                    current_ingredients.append(text)
        if current_ingredients:
            groups.append(IngredientGroup(current_ingredients, current_purpose))
        return groups

    def instructions(self):
        lines = []
        for item in self._recipe_data().get("recipe_directions", []):
            if item.get("type") == "heading":
                text = normalize_string(item.get("heading_text", ""))
                if text:
                    lines.append(text)
            else:
                text = normalize_string(item.get("direction", ""))
                if text:
                    lines.append(text)
        return "\n".join(lines)
