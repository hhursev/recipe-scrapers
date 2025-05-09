from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup
from ._utils import normalize_string


class VarechaPravdaSK(AbstractScraper):
    @classmethod
    def host(cls):
        return "varecha.pravda.sk"

    def ingredient_groups(self):
        results = {}
        ingredients_table = self.soup.find(attrs={'suroviny'}).table
        purpose = None
        for row in ingredients_table.findChildren("tr"):
            ingredient_group = row.find(attrs='recipe-ingredients__group')
            if ingredient_group:
                purpose = ingredient_group.text.strip()
                results[purpose] = IngredientGroup([], purpose=purpose)
            else:
                ingredient_name = (
                    normalize_string(row.find(attrs={"class": "recipe-ingredients__ingredient"}).get_text())
                )
                ingredient_amount = (
                    normalize_string(row.find(attrs={"class": "recipe-ingredients__amount"}).get_text())
                )
                if ingredient_amount:
                    ingredient_name = f"{ingredient_name}: {ingredient_amount}"
                if purpose:
                    results[purpose].ingredients.append(ingredient_name)
                else:
                    if "" not in results:
                        results[""] = IngredientGroup([], purpose=None)
                    results[""].ingredients.append(ingredient_name)
        return list(results.values())
