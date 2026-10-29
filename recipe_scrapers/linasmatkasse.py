import json

from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup


class LinasMatkasse(AbstractScraper):
    @classmethod
    def host(cls):
        return "linasmatkasse.se"

    def author(self):
        return self.schema.author() or self.site_name()

    def ingredient_groups(self):
        ingredients = self.ingredients()
        sections = self._ingredient_sections()
        if not sections or sum(
            len(section["ingredients"]) for section in sections
        ) != len(ingredients):
            return [IngredientGroup(ingredients=ingredients)]

        groups = []
        start = 0
        for section in sections:
            end = start + len(section["ingredients"])
            groups.append(
                IngredientGroup(
                    ingredients=ingredients[start:end],
                    purpose=section.get("sectionTitle") or None,
                )
            )
            start = end
        return groups

    def _ingredient_sections(self):
        # The page embeds the full recipe, one entry per portion size, in the
        # Next.js data. Unlike the rendered HTML, it also includes pantry items
        # (e.g. salt, olivolja) within their sections, matching the schema.
        script_tag = self.soup.find("script", {"id": "__NEXT_DATA__"})
        if not script_tag or not script_tag.string:
            return None
        try:
            queries = json.loads(script_tag.string)["props"]["pageProps"][
                "initialState"
            ]["api"]["queries"]
        except (ValueError, KeyError, TypeError):
            return None

        recipe = next(
            (
                query.get("data", {}).get("recipeAndSteps")
                for key, query in queries.items()
                if key.startswith("recipeAndSteps")
            ),
            None,
        )
        if not recipe:
            return None

        size = (self.yields() or "").split(" ")[0]
        portion = next(
            (
                portion
                for portion in recipe.get("instructions", {}).get("portions", [])
                if portion.get("size") == size
            ),
            None,
        )
        return portion.get("ingredientSections") if portion else None
