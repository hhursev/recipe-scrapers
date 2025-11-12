from ._abstract import AbstractScraper
from ._utils import normalize_string
from ._grouping_utils import IngredientGroup


class CarriesExperimentalKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "carriesexperimentalkitchen.com"

    def equipment(self):
        equipment_header = self.soup.find(
            "h4", string=lambda t: t and "equipment needed" in t.lower()
        )
        if equipment_header:
            equipment_list = equipment_header.find_next(
                "ul", class_="wprm-recipe-ingredients"
            )
            if equipment_list:
                return [
                    normalize_string(li.get_text())
                    for li in equipment_list.find_all("li")
                ]
        return []

    def ingredient_groups(self):
        groups = []
        ingredient_groups_html = self.soup.select(".wprm-recipe-ingredient-group")

        for group in ingredient_groups_html:
            heading = group.select_one(".wprm-recipe-ingredient-group-name")
            purpose = heading.get_text(strip=True) if heading else None

            # Skip the Equipment section
            if purpose and "equipment" in purpose.lower():
                continue

            ingredients = []
            for el in group.select(".wprm-recipe-ingredient"):
                parts = []
                amount = el.select_one(".wprm-recipe-ingredient-amount")
                unit = el.select_one(".wprm-recipe-ingredient-unit")
                name = el.select_one(".wprm-recipe-ingredient-name")
                notes = el.select_one(".wprm-recipe-ingredient-notes")
                if amount:
                    parts.append(amount.get_text(strip=True))
                if unit:
                    parts.append(unit.get_text(strip=True))
                if name:
                    parts.append(name.get_text(strip=True))
                if notes:
                    parts.append(notes.get_text(strip=True))
                ingredient = " ".join(parts)
                ingredient = " ".join(ingredient.split())
                ingredients.append(ingredient)

            groups.append(IngredientGroup(ingredients=ingredients, purpose=purpose))

        if groups:
            return groups
        else:
            return [IngredientGroup(ingredients=self.ingredients())]

    def ingredients(self):
        ingredients = []
        ingredient_container = self.soup.find(
            "div", class_="wprm-recipe-ingredients-container"
        )
        if not ingredient_container:
            return ingredients

        for group in ingredient_container.find_all(
            "div", class_="wprm-recipe-ingredient-group"
        ):
            header = group.find("h4", class_="wprm-recipe-group-name")
            name = normalize_string(header.get_text()) if header else ""
            if "equipment" in name.lower():
                continue
            for li in group.find_all("li", class_="wprm-recipe-ingredient"):
                ingredients.append(normalize_string(li.get_text()))
        return ingredients
