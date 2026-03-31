from ._abstract import AbstractScraper
from ._utils import get_yields
import re
from ._grouping_utils import IngredientGroup


class Argiro(AbstractScraper):
    @classmethod
    def host(cls):
        return "argiro.gr"

    def author(self):
        return "Αργυρώ Μπαρμπαρίγου"

    def title(self):
        return self.soup.select_one("h1.single_recipe__title").get_text(strip=True)

    def description(self):
        meta_description = self.soup.select_one('meta[name="description"]')
        return meta_description.get("content", "")

    def category(self):
        return [
            a.get_text(strip=True)
            for a in self.soup.select(".article__tags ul li.tag_item a")
        ]

    def _parse_time(self, selector):
        element = self.soup.select_one(selector)
        if not element:
            return 0
        text = element.get_text(strip=True)
        hours = int(re.search(r"(\d+)\s*ώρα", text).group(1)) if "ώρα" in text else 0
        minutes = (
            int(re.search(r"(\d+)\s*λεπτά", text).group(1)) if "λεπτά" in text else 0
        )
        return hours * 60 + minutes

    def prep_time(self):
        return self._parse_time(".item.preparation_time h2.item__title")

    def cook_time(self):
        return self._parse_time(".item.cooking_time h2.item__title")

    def total_time(self):
        prep_time = self.prep_time()
        cook_time = self.cook_time()
        if prep_time == 0 or cook_time == 0:
            return None
        return prep_time + cook_time

    def equipment(self):
        equipment_items = self.soup.select(".equipment__item h2.equipment__item__name")
        return [item.get_text(strip=True) for item in equipment_items]

    def yields(self):
        yields = self.soup.select_one(".item.portions h2.item__title")
        return get_yields(yields.get_text(strip=True))

    def ingredients(self):
        results = []
        containers = self.soup.select("div.single_recipe__left_column div.ingredients")

        for container in containers:
            for section in container.select(".ingredients__container"):
                items = section.select(".ingredients__item label.ingredient-label")
                for label in items:
                    quantity = label.select_one(".ingredients__quantity")
                    name = label.select_one("p")
                    text = ""
                    if quantity:
                        text += quantity.get_text(strip=True) + " "
                    if name:
                        text += name.get_text(strip=True)
                    results.append(text.strip())
        return results

    def ingredient_groups(self):
        groups = []
        containers = self.soup.select("div.single_recipe__left_column div.ingredients")

        for container in containers:
            sections = container.select(".ingredients__title")
            containers_by_section = container.select(".ingredients__container")

            for title, section in zip(sections, containers_by_section):
                raw_purpose = title.get_text(strip=True)
                purpose = raw_purpose if raw_purpose else None

                group_ingredients = []
                items = section.select(".ingredients__item label.ingredient-label")
                for label in items:
                    quantity = label.select_one(".ingredients__quantity")
                    name = label.select_one("p")
                    text = ""
                    if quantity:
                        text += quantity.get_text(strip=True) + " "
                    if name:
                        text += name.get_text(strip=True)
                    group_ingredients.append(text.strip())

                groups.append(
                    IngredientGroup(ingredients=group_ingredients, purpose=purpose)
                )

            # Fallback: handle case with no group titles
            if not sections and containers_by_section:
                for section in containers_by_section:
                    group_ingredients = []
                    items = section.select(".ingredients__item label.ingredient-label")
                    for label in items:
                        quantity = label.select_one(".ingredients__quantity")
                        name = label.select_one("p")
                        text = ""
                        if quantity:
                            text += quantity.get_text(strip=True) + " "
                        if name:
                            text += name.get_text(strip=True)
                        group_ingredients.append(text.strip())

                    if group_ingredients:
                        groups.append(
                            IngredientGroup(ingredients=group_ingredients, purpose=None)
                        )

        return groups

    def instructions(self):
        steps = self.soup.select(".single_recipe__method_steps ol li")
        cleaned_steps = []
        punctuation = [".", ",", ";", "!", "?", ":", "·", "…", "–"]
        for step in steps:
            text = step.get_text(" ", strip=True).replace("  ", " ")
            for punct in punctuation:
                text = text.replace(f" {punct}", punct)
            cleaned_steps.append(text)
        return "\n".join(cleaned_steps)
