from ._abstract import AbstractScraper
from ._utils import normalize_string


class Bofrost(AbstractScraper):
    @classmethod
    def host(cls):
        return "bofrost.de"

    def nutrients(self):
        self._nutrients = self.soup.select_one(".recipe-nutrations")

        def _get_nutrient(nutrient_name):
            if self._nutrients:
                for row in self._nutrients.select(".row"):
                    key_element = row.select(".col-6.recipe-nutrations-item")
                    if len(key_element) == 2:
                        key = key_element[0].get_text(strip=True).replace(":", "")
                        value = key_element[1].get_text(strip=True)
                        if key == nutrient_name:
                            return normalize_string(value)
            return None

        nutrients = {
            "calories": _get_nutrient("Kalorien"),
            "fatContent": _get_nutrient("Fett"),
            "saturatedFatContent": _get_nutrient("Gesättigte Fette"),
            "carbohydrateContent": _get_nutrient("Kohlenhydrate"),
            "sugarContent": _get_nutrient("Zucker"),
            "proteinContent": _get_nutrient("Eiweiß"),
            "sodiumContent": _get_nutrient("Salz"),
            "fiberContent": _get_nutrient("Ballaststoffe"),
        }

        return {key: value for key, value in nutrients.items() if value is not None}
