from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class InGoodFlavor(AbstractScraper):
    @classmethod
    def host(cls):
        return "ingoodflavor.com"

    def author(self):
        signature_div = self.soup.find("div", class_="text-signature")
        signature_text = signature_div.get_text(strip=True) if signature_div else None
        schema_author = self.schema.author()

        if signature_text and schema_author:
            return f"{signature_text} | {schema_author}"
        return schema_author

    def ingredient_groups(self):
        groups = group_ingredients(
            self.ingredients(),
            self.soup,
            ".dr-title",
            ".dr-ingredient-name",
        )

        for group in groups:
            if group.purpose and group.purpose.strip().lower() == "ingredients":
                group.purpose = None

        return groups
