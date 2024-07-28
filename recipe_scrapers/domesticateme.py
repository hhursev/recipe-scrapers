from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class DomesticateMe(AbstractScraper):
    @classmethod
    def host(cls):
        return "domesticate-me.com"

    def author(self):
        author_from_schema = self.schema.author()
        if author_from_schema:
            return author_from_schema

        author_meta_tag = self.soup.find("meta", {"name": "author"})
        author_name = author_meta_tag["content"] if author_meta_tag else None
        return author_name

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient-group li",
        )
