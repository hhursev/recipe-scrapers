from ._abstract import AbstractScraper


class GialloZafferano(AbstractScraper):
    @classmethod
    def host(cls):
        return "ricette.giallozafferano.it"

    def ingredients(self):
        ingredients = []

        units = {
            "g",
            "kg",
            "mg",
            "ml",
            "l",
            "cl",
        }

        for ingredient in self.soup.select("dd.gz-ingredient"):
            name = ingredient.find("a").get_text(" ", strip=True)

            amount = ingredient.find("span").get_text(" ", strip=True)
            amount = " ".join(amount.split())

            parts = amount.split()

            if len(parts) == 2 and parts[1] in units:
                amount = f"{parts[0]}{parts[1]}"

            ingredients.append(f"{amount} {name}".strip())

        return ingredients

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
