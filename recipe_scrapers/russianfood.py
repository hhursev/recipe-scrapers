from ._abstract import AbstractScraper
import re
from ._grouping_utils import IngredientGroup


class RussianFood(AbstractScraper):
    @classmethod
    def host(cls):
        return "russianfood.com"

    def author(self):
        author = self.soup.select_one(".sub_info .user_date a")
        return author.get_text(" ", strip=True) if author else "RussianFood"

    def title(self):
        return self.soup.find("h1").get_text().strip()

    def ingredients(self):
        ingr_table = self.soup.find("table", class_="ingr")
        if not ingr_table:
            return []

        ingredients = []
        for row in ingr_table.find_all("tr", class_=re.compile(r"ingr_tr_\d+")):
            text = row.get_text(" ", strip=True)

            if text and text != "*" and not text.endswith(":"):
                ingredients.append(text)

        return ingredients

    def instructions(self):
        steps = self.soup.find_all("div", {"class": "step_n"})
        result = []
        for step in steps:
            p = step.find("p")
            if p:
                text = p.get_text(strip=True)
                if text:
                    result.append(text)
        return "\n".join(result)

    def image(self):
        og_image = self.soup.find("meta", {"property": "og:image"})
        if og_image:
            return og_image.get("content")
        return None

    def ingredient_groups(self):
        groups = []
        purpose = None
        ingredients = []

        ingr_table = self.soup.find("table", class_="ingr")
        if not ingr_table:
            return []

        for row in ingr_table.find_all("tr", class_=re.compile(r"ingr_tr_\d+")):
            text = row.get_text(" ", strip=True)

            if not text or text == "*":
                continue

            if text.endswith(":"):
                if ingredients:
                    groups.append(
                        IngredientGroup(
                            ingredients=ingredients,
                            purpose=purpose,
                        )
                    )
                purpose = text.rstrip(":")
                ingredients = []
            else:
                ingredients.append(text)

        if ingredients:
            groups.append(
                IngredientGroup(
                    ingredients=ingredients,
                    purpose=purpose,
                )
            )

        return groups
