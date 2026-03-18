from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup


class StreetKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "streetkitchen.hu"

    def ingredients(self):
        ingredients_list = []
        for item in self.soup.select(
            "div.w-full.rounded-b-md div.my-2.flex.items-center.gap-2.text-lg"
        ):
            divs = [
                child
                for child in item.children
                if getattr(child, "name", None) == "div"
            ]
            parts = [
                div.get_text(" ", strip=True)
                for div in divs
                if div.get_text(strip=True)
            ]
            if parts:
                text = " ".join(parts)
                text = text.replace("( ", "(").replace(" )", ")")
                ingredients_list.append(text)
        return ingredients_list

    def ingredient_groups(self):
        groups = []
        for group_block in self.soup.select("div.w-full.rounded-b-md > div > div"):
            heading_tag = group_block.select_one("h5.text-lg.font-bold")
            purpose = heading_tag.get_text(strip=True) if heading_tag else None

            if purpose == "":
                return [IngredientGroup(ingredients=self.ingredients())]

            ingredients = []
            for item in group_block.select("div.my-2.flex.items-center.gap-2.text-lg"):
                divs = [
                    child
                    for child in item.children
                    if getattr(child, "name", None) == "div"
                ]
                parts = [
                    div.get_text(" ", strip=True)
                    for div in divs
                    if div.get_text(strip=True)
                ]
                if parts:
                    text = " ".join(parts)
                    text = text.replace("( ", "(").replace(" )", ")")
                    ingredients.append(text)

            if ingredients:
                groups.append(IngredientGroup(ingredients=ingredients, purpose=purpose))

        if not groups:
            return [IngredientGroup(ingredients=self.ingredients())]
        return groups

    def instructions(self):
        container = self.soup.select_one(
            "article.recipe-article"
        ) or self.soup.select_one("div.recipe-article")
        if not container:
            return ""

        instructions = []
        for child in container.children:
            if getattr(child, "name", None) in ["p", "span"]:
                text = child.get_text(" ", strip=True)
                if text:
                    instructions.append(text)
            elif getattr(child, "name", None) in ["h2", "h3", "figure"]:
                continue
            elif getattr(child, "name", None) is not None:
                break

        return "\n".join(instructions)
