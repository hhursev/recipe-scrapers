from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup


class ReceptyPreVas(AbstractScraper):
    @classmethod
    def host(cls):
        return "receptyprevas.sk"

    def description(self):
        description = []
        p_list = self.soup.find("div", {"class": "single-content-self"}).findChildren(
            "p"
        )
        for p in p_list:
            text = p.get_text().strip()
            if text:
                description.append(text)
        return " ".join(description)

    def ingredient_groups(self):
        results = {}
        ingredients_div = self.soup.find("table", {"class": "ingredients-table"})
        purpose = None
        for row in ingredients_div.findChildren("tr"):
            if row.find("div", {"class": "ingredient-heading"}):
                purpose = row.get_text().strip()
                results[purpose] = IngredientGroup([], purpose=purpose)
            else:
                ingredient_name = (
                    row.find("span", {"class": "ingredient-name"}).get_text().strip()
                )
                ingredient_amount = (
                    row.find("span", {"class": "ingredient-amount"}).get_text().strip()
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
