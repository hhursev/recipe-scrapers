from ._abstract import AbstractScraper
from ._utils import normalize_string


class GialloZafferano(AbstractScraper):
    @classmethod
    def host(cls):
        return "ricette.giallozafferano.it"

    def ingredients(self):
        ingredients = []
        for item in self.soup.select("dd.gz-ingredient"):
            span = item.find("span")
            quantity = normalize_string(span.get_text()) if span else ""
            name = normalize_string(
                " ".join(
                    text
                    for text in item.find_all(string=True)
                    if not text.find_parent("span")
                )
            )
            # the site lists quantities after the name; put numeric ones first
            if quantity[:1].isnumeric():
                ingredients.append(f"{quantity} {name}")
            else:
                ingredients.append(normalize_string(f"{name} {quantity}"))
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
