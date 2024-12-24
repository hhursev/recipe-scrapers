from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class Bakels(AbstractScraper):
    @classmethod
    def host(cls, domain="com.au"):
        return f"bakels.{domain}"

    def author(self):
        return self.site_name()

    def title(self):
        return self.soup.find("h1").get_text()

    def ingredients(self):
        div = self.soup.find("div", id="tab-ingredients_1")
        if not div:
            return

        results = []
        groups = div.find_all("div", {"class": "row"})
        for group in groups:
            ingredients = group.find_all(class_="text-xs-left")
            for ingredient in ingredients:
                text = ingredient.get_text(strip=True)
                if text == "Ingredient" or text.startswith("Group"):
                    continue  # Ensures these headings are not included as ingredients
                results.append(text)
        return results

    def ingredient_groups(self):
        groups = group_ingredients(
            self.ingredients(),
            self.soup,
            ".group-label",
            "#tab-ingredients_1 .text-xs-left:not(:-soup-contains('Ingredient')):not(:-soup-contains('Group'))",
        )

        if len(groups) == 1:
            groups[0].purpose = None

        return groups

    def instructions(self):
        div = self.soup.find("div", id="tab-method_1")
        if not div:
            return None

        tag = div.find("p")
        if not tag:
            return None

        instructions = div.get_text(separator="\n", strip=True)
        instructions = "\n".join(
            step.split(". ", 1)[-1] for step in instructions.split("\n")
        )  # Removes the instruction number from each step
        return instructions

    def description(self):
        description_meta = self.soup.find("meta", {"property": "og:title"})
        if description_meta:
            return description_meta.get("content")
        return None

    def category(self):
        category_h4 = self.soup.find("h4", string="Category")
        if not category_h4:
            return None

        category_p = category_h4.find_next_sibling("p")
        if not category_p:
            return None

        return category_p.text
