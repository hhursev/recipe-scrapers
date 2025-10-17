from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class NinjaTestKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "ninjatestkitchen.eu"

    def author(self):
        return "Ninja Test Kitchen"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup.select_one('div.single-ingredients__group[data-unit="imperial"]'),
            "div.single-ingredients__item > h4.single-ingredients__title",
            "div.single-ingredients__item ul.single-ingredients__list li",
        )

    def ingredients(self):
        ingredients = []
        group = self.soup.select_one(
            'div.single-ingredients__group[data-unit="imperial"]'
        )

        if group:
            items = group.select("div.single-ingredients__item")
            for item in items:
                ul = item.select_one("ul.single-ingredients__list")
                if ul:
                    for li in ul.select("li"):
                        quantity = li.select_one("span.font-weight-semi-bold")
                        text = li.get_text(strip=True)
                        if quantity:
                            quantity_text = quantity.get_text(strip=True)
                            ingredient_text = text.replace(quantity_text, "", 1).strip()
                            ingredients.append(f"{quantity_text} {ingredient_text}")
                        else:
                            ingredients.append(text)
        return ingredients

    def instructions(self):
        instructions = []
        method_list = self.soup.select_one("ul.single-method__method")

        if method_list:
            for li in method_list.select("li"):
                step = li.select_one("p")
                if step:
                    text = step.get_text()
                    parts = text.split(". ", 1)
                    if len(parts) == 2 and parts[0].isdigit():
                        text = parts[1]
                    instructions.append(text)
        return "\n".join(instructions)

    def equipment(self):
        equipment = []
        items = self.soup.select("ul.products-list li.product")

        for item in items:
            name_tag = item.select_one("div.name-container h3")
            if name_tag:
                equipment.append(name_tag.get_text(strip=True))
        return equipment

    def keywords(self):
        keywords = []
        keywords_container = self.soup.select_one("div.single-hero__title h6")

        if keywords_container:
            for link in keywords_container.select("a[href*='/recipe_cat/']"):
                keywords.append(link.get_text(strip=True))
        return keywords
