from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class InGoodFlavor(AbstractScraper):
    @classmethod
    def host(cls):
        return "ingoodflavor.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".dr-title",
            ".dr-ingredient-name",
        )

    def author(self):
        signature_div = self.soup.find("div", class_="text-signature")
        signature_text = signature_div.get_text(strip=True) if signature_div else ""

        schema_author = self.schema.author()

        if signature_text:
            return f"{signature_text} | {schema_author}"

        return schema_author
