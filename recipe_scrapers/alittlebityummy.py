from ._abstract import AbstractScraper
from ._utils import normalize_string, get_minutes
from ._grouping_utils import IngredientGroup


class ALittleBitYummy(AbstractScraper):
    @classmethod
    def host(cls):
        return "alittlebityummy.com"

    def author(self):
        author_tag = self.soup.find(
            "h4", string=lambda text: text and "Author:" in text
        )
        if author_tag:
            return author_tag.text.replace("Author:", "").strip()

    def ingredients(self):
        ingredient_blocks = self.soup.select(
            ".ingredients-tab-content div:has(b.ingredient-unit-display)"
        )

        seen = set()
        ingredients = []

        for block in ingredient_blocks:
            unit_display = block.find("b", class_="ingredient-unit-display")
            name_display = block.find("span", class_="ingredient-name-display")

            if not unit_display or not name_display:
                continue

            primary_amount = unit_display.get("data-primary-amount", "").strip()
            primary_unit = unit_display.get("data-primary-unit", "").strip()

            secondary_amount = unit_display.get("data-secondary-amount", "").strip()
            secondary_unit = unit_display.get("data-secondary-unit", "").strip()

            amount_text = f"{primary_amount} {primary_unit}".strip()
            if secondary_amount:
                amount_text += f" ({secondary_amount} {secondary_unit})"

            name = name_display.get_text(strip=True)
            full_ingredient = f"{amount_text} {name}".strip()

            if full_ingredient not in seen:
                seen.add(full_ingredient)
                ingredients.append(full_ingredient)

        return ingredients

    def instructions(self):
        instruction_steps = self.soup.select("#method ol li")
        return "\n".join(
            normalize_string(step.get_text())
            for step in instruction_steps
            if step.get_text()
        )

    def ingredient_groups(self):
        ingredients = self.ingredients()
        groups = []

        current_purpose = None
        current_ingredients = []
        ing_idx = 0

        nodes = self.soup.select(
            ".ingredients-tab-content h4.highlighted, "
            ".ingredients-tab-content div:has(b.ingredient-unit-display)"
        )

        for node in nodes:
            if node.name == "h4":
                if current_ingredients:
                    groups.append(
                        IngredientGroup(
                            ingredients=current_ingredients,
                            purpose=current_purpose,
                        )
                    )
                    current_ingredients = []
                current_purpose = node.get_text(strip=True)

            else:
                if ing_idx < len(ingredients):
                    current_ingredients.append(ingredients[ing_idx])
                    ing_idx += 1

        if current_ingredients:
            groups.append(
                IngredientGroup(
                    ingredients=current_ingredients,
                    purpose=current_purpose,
                )
            )

        if len(groups) <= 1:
            return [IngredientGroup(ingredients=ingredients, purpose=None)]

        return groups

    def prep_time(self):
        meta = self.soup.select_one(".recipe-meta")
        if not meta:
            return None

        for span in meta.find_all("span"):
            if "PREP IN" in span.get_text():
                value = span.find("span")
                if value:
                    return get_minutes(value.get_text(strip=True).lower())
        return None

    def cook_time(self):
        meta = self.soup.select_one(".recipe-meta")
        if not meta:
            return None

        for span in meta.find_all("span"):
            if "COOKS IN" in span.get_text():
                value = span.find("span")
                if value:
                    return get_minutes(value.get_text(strip=True).lower())
        return None

    def total_time(self):
        prep = self.prep_time()
        cook = self.cook_time()
        if prep is None and cook is None:
            return None
        prep_minutes = prep if prep is not None else 0
        cook_minutes = cook if cook is not None else 0
        total = prep_minutes + cook_minutes
        return total if total else None

    def nutrients(self):
        meta = self.soup.select_one(".recipe-nutrition")
        if not meta:
            return None

        tab = meta.select_one(".nutrition-tab-content.current") or meta.select_one(
            ".nutrition-tab-content"
        )
        if not tab:
            return None

        mapping = {
            "calories": "calories",
            "fat": "fatContent",
            "saturates": "saturatedFatContent",
            "protein": "proteinContent",
            "carbs": "carbohydrateContent",
            "sugars": "sugarContent",
            "fibre": "fiberContent",
            "salt": "sodiumContent",
            "cholesterol": "cholesterolContent",
            "trans fat": "transFatContent",
            "unsaturated fat": "unsaturatedFatContent",
        }

        def clean_nutrient_value(v):
            if not v:
                return None
            v = v.strip()
            v = "".join(ch for ch in v if (ch.isdigit() or ch == "."))
            return v if v else None

        nutrients = {}

        for block in tab.select(".nutrition-block"):
            name_el = block.select_one(".nutrition-name")
            value_el = block.select_one(".nutrition-weight")

            if not name_el or not value_el:
                continue

            name_raw = name_el.get_text(strip=True).lower()
            value_raw = value_el.get_text(strip=True)

            value = clean_nutrient_value(value_raw)

            key = None
            for k in mapping:
                if k in name_raw:
                    key = mapping[k]
                    break

            if key:
                nutrients[key] = value
            else:
                nutrients[name_raw] = value

        return nutrients if nutrients else None
