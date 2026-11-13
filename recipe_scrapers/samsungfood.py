import json
import re

from ._abstract import AbstractScraper
from ._exceptions import FillPluginException, SchemaOrgException
from ._utils import get_yields


class SamsungFood(AbstractScraper):
    @classmethod
    def host(cls):
        return "app.samsungfood.com"

    def title(self):
        return self._value("title", "name")

    def author(self):
        if author := self._schema_value("author"):
            return author
        author = self._hydrate_value("recipeAuthor", "author", "value")
        name = author.get("name") or " ".join(
            part for part in (author.get("firstName"), author.get("lastName")) if part
        )
        if not name:
            raise FillPluginException("No author name in Samsung Food hydration")
        return name

    def site_name(self):
        return self._schema_value("site_name") or "Samsung Food"

    def category(self):
        return self._schema_value("category") or self._labels("mealType")

    def yields(self):
        return self._schema_value("yields") or get_yields(
            self._hydrate_value("servings")
        )

    def description(self):
        return self._value("description", "description")

    def total_time(self):
        if (total := self._schema_value("total_time")) is not None:
            return total
        durations = self._hydrate_value("durations")
        if "totalTime" in durations:
            return durations["totalTime"]
        if not durations.keys() & {"prepTime", "cookTime"}:
            raise FillPluginException("No cooking times in Samsung Food hydration")
        return (durations.get("prepTime") or 0) + (durations.get("cookTime") or 0)

    def cook_time(self):
        return self._value("cook_time", "durations", "cookTime")

    def prep_time(self):
        return self._value("prep_time", "durations", "prepTime")

    def cuisine(self):
        return self._schema_value("cuisine") or self._labels("cuisine")

    def cooking_method(self):
        return self._schema_value("cooking_method") or self._labels("technique")

    def image(self):
        return self._value("image", "images", 0, "url")

    def keywords(self):
        if keywords := self._schema_value("keywords"):
            return keywords
        labels = self._hydrate_value("labels")
        return list(
            dict.fromkeys(
                [self.title()]
                + [
                    self._inside(label, "displayName")
                    for group in ("mealType", "cuisine")
                    for label in labels.get(group, [])
                ]
            )
        )

    def ratings_count(self):
        if (count := self._schema_value("ratings_count")) is not None:
            return count
        rating = self._hydrate_value("reviews", "rating")
        return rating.get("likeCount", 0) + rating.get("dislikeCount", 0)

    def ingredients(self):
        ingredients = self._schema_value("ingredients")
        if ingredients is None:
            ingredients = [
                self._inside(ingredient, "text")
                for ingredient in self._hydrate_value("ingredients")
            ]
        return [ingredient.lstrip("- ").strip() for ingredient in ingredients]

    def instructions(self):
        instructions = self._schema_value("instructions")
        if instructions is None:
            instructions = "\n".join(
                self._inside(step, "text")
                for step in self._hydrate_value("instructions", "steps")
            )
        return "\n".join(
            re.sub(r"^\d+\.\s*", "", line).strip() for line in instructions.split("\n")
        )

    def nutrients(self):
        if nutrients := self._schema_value("nutrients"):
            cleaned = {}
            for key, value in nutrients.items():
                if "calories" in key.lower():
                    if match := re.search(r"\d+(\.\d+)?", value):
                        cleaned["calories"] = match.group(0)
                else:
                    cleaned[key] = value.strip('"')
            return cleaned

        # Schema nutrition uses named fields, e.g. {"fatContent": "12.5 g"}.
        # Hydration instead supplies nutrition.components entries such as:
        # {"code": {"name": "FAT"}, "value": 12.5,
        #  "unit": {"displayName": "g"}}
        # ENERC_KCAL becomes a unitless "calories" value, as in schema cleanup.
        nutrient_keys = {
            "ENERC_KCAL": "calories",
            "FAT": "fatContent",
            "FASAT": "saturatedFatContent",
            "FATRN": "transFatContent",
            "CHOCDF": "carbohydrateContent",
            "SUGAR": "sugarContent",
            "PROCNT": "proteinContent",
            "FIBTG": "fiberContent",
            "CHOLE": "cholesterolContent",
            "NA": "sodiumContent",
        }
        nutrients = {}
        for component in self._hydrate_value("nutrition", "components"):
            key = nutrient_keys.get(self._inside(component, "code", "name"))
            if key is None:
                continue
            value = f"{self._inside(component, 'value'):.2f}".rstrip("0").rstrip(".")
            if key != "calories":
                value += f" {self._inside(component, 'unit', 'displayName')}"
            nutrients[key] = value
        if not nutrients:
            raise FillPluginException("No nutrients in Samsung Food hydration")
        return nutrients

    def _schema_value(self, method):
        if not self.schema.data or (
            method == "title" and not self.schema.data.get("name")
        ):
            return None
        try:
            value = getattr(self.schema, method)()
        except SchemaOrgException:
            return None
        return None if value in (None, "", [], {}) else value

    def _value(self, method, *keys):
        value = self._schema_value(method)
        return value if value is not None else self._hydrate_value(*keys)

    def _labels(self, group):
        labels = self._hydrate_value("labels", group)
        if not labels:
            raise FillPluginException(f"No {group} in Samsung Food hydration")
        return ",".join(self._inside(label, "displayName") for label in labels)

    def _hydrate_value(self, *keys):
        if not hasattr(self, "_recipe"):
            self._recipe = self._parse_hydrate()
        return self._inside(self._recipe, *keys)

    @staticmethod
    def _inside(value, *keys):
        try:
            for key in keys:
                value = value[key]
        except (KeyError, IndexError, TypeError) as error:
            raise FillPluginException(
                f"Missing Samsung Food hydration field: {keys}"
            ) from error
        if value is None or value == "":
            raise FillPluginException(f"Empty Samsung Food hydration field: {keys}")
        return value

    def _parse_hydrate(self):
        """Read the embedded recipe when Recipe schema cannot supply a field.

        Schema-backed pages expose JSON-LD in an application/ld+json script:
            {"@type": "Recipe", "name": "Granola",
             "recipeIngredient": ["1 cup oats"], "prepTime": "PT10M"}

        Native recipes may omit that schema but include a JavaScript assignment:
            var hydrate = {
                "whisk.x.recipe.v1.RecipeAPI/GetRecipe_<request bytes>": {
                    "recipe": {
                        "id": "107...", "name": "Granola",
                        "ingredients": [{"text": "1 cup oats"}],
                        "instructions": {"steps": [{"text": "1. Mix."}]},
                        "durations": {"prepTime": 10}, "servings": 1
                    }
                }
            };

        The RPC key suffix varies by request, not just recipe ID. Other entries
        contain user data and recommendations, so only GetRecipe results qualify.
        Decode the JSON value without executing JavaScript or its trailing suffix.
        """
        for script in self.soup.find_all("script"):
            match = re.match(r"\s*var\s+hydrate\s*=\s*", script.string or "")
            if not match:
                continue
            try:
                hydrate, _ = json.JSONDecoder().raw_decode(script.string[match.end() :])
            except json.JSONDecodeError as error:
                raise FillPluginException(
                    "Invalid Samsung Food hydration JSON"
                ) from error
            if not isinstance(hydrate, dict):
                raise FillPluginException("Invalid Samsung Food hydration object")
            recipes = [
                value["recipe"]
                for key, value in hydrate.items()
                if key.startswith("whisk.x.recipe.v1.RecipeAPI/GetRecipe_")
                and isinstance(value, dict)
                and isinstance(value.get("recipe"), dict)
            ]
            recipe_id = re.search(r"/recipes/([^/?#]+)", self.canonical_url())
            if recipe_id:
                for recipe in recipes:
                    if recipe.get("id") == recipe_id.group(1):
                        return recipe
            elif len(recipes) == 1:
                return recipes[0]
        raise FillPluginException("No Samsung Food recipe hydration found")
