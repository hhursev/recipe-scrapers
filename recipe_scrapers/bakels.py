# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class Bakels(AbstractScraper):
    @classmethod
    def host(cls):
        return "bakels.com.au"

    def author(self):
        return "Australian Bakels"

    def title(self):
        return self.soup.find("h1").get_text()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        div = self.soup.find("div", id="tab-ingredients_1")
        if div:
            ingredients = div.find_all(class_="text-xs-left")
            array = []
            flag = False
            for ingredient in ingredients:
                text = ingredient.get_text(strip=True)
                if text == "Ingredient":
                    flag = True
                elif flag:
                    array.append(text)
            return array

    def instructions(self):
        div = self.soup.find("div", id="tab-method_1")
        if div:
            tag = div.find("p")
            if tag:
                instructions = tag.get_text(separator="\n", strip=True)
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
        category_p = category_h4.find_next_sibling("p")
        return category_p.text
