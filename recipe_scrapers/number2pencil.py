# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class Number2Pencil(AbstractScraper):
    @classmethod
    def host(cls):
        return "number-2-pencil.com"

    def author(self):
        author_from_schema = self.schema.author()
        if author_from_schema:
            return author_from_schema

        author_span = self.soup.find("span", {"class": "entry-author"})
        author_name = (
            author_span.find("span", {"class": "entry-author-name"})
            if author_span
            else None
        )
        return author_name.text if author_name else "number-2-pencil"

    def category(self):
        category_from_schema = self.schema.category()
        if category_from_schema:
            return category_from_schema

        entry_categories_div = self.soup.find("span", {"class": "entry-categories"})
        categories = [a.text for a in entry_categories_div.find_all("a", href=True)]
        return ", ".join(categories)

    def description(self):
        description_from_schema = self.schema.description()
        if description_from_schema:
            return description_from_schema

        entry_content_div = self.soup.find("div", {"class": "entry-content"})
        return entry_content_div.find("em").text

    def cuisine(self):
        return self.schema.cuisine()

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def ingredient_groups(self):
        return group_ingredients(
            ingredients_list=self.ingredients(),
            soup=self.soup,
            group_heading="div.wprm-recipe-ingredient-group-name",
            group_element="li.wprm-recipe-ingredient",
        )

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()
