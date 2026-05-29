from ._abstract import AbstractScraper


class GialloZafferano(AbstractScraper):
    @classmethod
    def host(cls):
        return "ricette.giallozafferano.it"

    def ingredients(self):
        ingredients = (
            self.schema.data.get("recipeIngredient")
            or self.schema.data.get("ingredients")
            or []
        )
        return [self._reverse_ingredient(ingredient) for ingredient in ingredients]

    def nutrients(self):
        nutrients = self.schema.data.get("nutrition", {})
        nutrient_keys = [
            "calories",
            "fatContent",
            "saturatedFatContent",
            "carbohydrateContent",
            "sugarContent",
            "sodiumContent",
            "fiberContent",
            "cholesterolContent",
        ]
        return {key: self._fix_comma(nutrients.get(key)) for key in nutrient_keys}

    def _fix_comma(self, value):
        if isinstance(value, str):
            return value.replace(",", ".").strip()
        return value
