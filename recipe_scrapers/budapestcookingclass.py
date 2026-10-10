from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup
from ._utils import normalize_string
from ._wprm import WPRMMixin


class BudapestCookingClass(WPRMMixin, AbstractScraper):
    def __init__(self, html: str, url: str, best_image: bool | None = None):
        # Page-wide image metadata includes unrelated cooking-class photos.
        super().__init__(
            html, url, best_image=False if best_image is None else best_image
        )

    @classmethod
    def host(cls):
        return "budapestcookingclass.com"

    def ingredient_groups(self) -> list[IngredientGroup]:
        cards = self.soup.select(".wprm-recipe-container")
        if not cards:
            return super().ingredient_groups()
        if len(cards) != 1:
            raise ValueError(
                "Expected one WP Recipe Maker recipe card for ingredient grouping."
            )

        groups = cards[0].select(".wprm-recipe-ingredient-group")
        if not groups:
            return super().ingredient_groups()

        ingredients = self.ingredients()
        counts = [len(group.select(".wprm-recipe-ingredient")) for group in groups]
        if sum(counts) != len(ingredients):
            raise ValueError(
                f"Found {sum(counts)} grouped ingredients but was expecting to find {len(ingredients)}."
            )

        # WPRM preserves schema order; position avoids ambiguous text matches.
        results = []
        offset = 0
        for group, count in zip(groups, counts):
            if not count:
                continue
            heading = group.select_one(".wprm-recipe-ingredient-group-name")
            results.append(
                IngredientGroup(
                    ingredients=ingredients[offset : offset + count],
                    purpose=(
                        normalize_string(heading.get_text()) or None
                        if heading
                        else None
                    ),
                )
            )
            offset += count
        return results or super().ingredient_groups()
