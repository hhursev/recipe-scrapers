from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup
from ._utils import normalize_string


class TheFlavorBender(AbstractScraper):
    @classmethod
    def host(cls):
        return "theflavorbender.com"

    def ingredient_groups(self) -> list[IngredientGroup]:
        ingredients = self.ingredients()
        groups = self.soup.select(".wprm-recipe-ingredient-group")
        if not groups:
            return [IngredientGroup(ingredients=ingredients)]

        counts = [len(group.select(".wprm-recipe-ingredient")) for group in groups]
        ingredient_count = sum(counts)
        if ingredient_count != len(ingredients):
            raise ValueError(
                f"Found {ingredient_count} grouped ingredients but was expecting to find {len(ingredients)}."
            )

        # WPRM preserves schema order; HTML-only notes can mislead fuzzy matching.
        result = []
        start = 0
        for group, count in zip(groups, counts):
            heading = group.select_one(".wprm-recipe-ingredient-group-name")
            end = start + count
            result.append(
                IngredientGroup(
                    ingredients=ingredients[start:end],
                    purpose=(
                        (normalize_string(heading.get_text()) or None)
                        if heading
                        else None
                    ),
                )
            )
            start = end
        return result
