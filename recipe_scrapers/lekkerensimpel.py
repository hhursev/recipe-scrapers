import re

from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml, SchemaOrgException
from ._utils import normalize_string


class LekkerEnSimpel(AbstractScraper):
    @classmethod
    def host(cls):
        return "lekkerensimpel.com"

    def author(self):
        return self.soup.find("meta", {"name": "author"})["content"]

    def title(self):
        title = self.soup.find("h1", {"class": "hero__title"}).text
        return normalize_string(title)

    def image(self):
        image = self.soup.find("meta", {"property", "og:image"})
        return image["content"] if image else None

    def ingredients(self):
        if self.schema.ingredients():
            return self.schema.ingredients()

        ingredient_header = self.soup.find("strong", string="Benodigdheden:")
        if ingredient_header:
            ingredients = ingredient_header.parent.parent.find_next("ul").findChildren(
                "li"
            )
            return [normalize_string(i.get_text()) for i in ingredients]

        ingredient_header = self.soup.find("p", string="Benodigdheden:")
        if ingredient_header:
            ingredients = ingredient_header.parent.find_next("ul").findChildren("li")
            return [normalize_string(i.get_text()) for i in ingredients]

        raise ElementNotFoundInHtml("Could not find ingredients.")

    def process_ingredients(self, container):
        ingredients = container.findChildren("li")

        return [normalize_string(i.get_text()) for i in ingredients]

    def instructions(self):
        if self.schema.instructions():
            return self.schema.instructions()

        instructions_head = self.soup.find("strong", string="Bereidingswijze:")
        if instructions_head:
            return instructions_head.parent.find_next("p")

        instructions_head = self.soup.find(string=re.compile("Bereidingswijze"))
        if instructions_head.parent:
            return instructions_head.parent.parent.text

        raise ElementNotFoundInHtml("Could not find instructions.")

    def description(self):
        try:
            return self.schema.description()
        except SchemaOrgException:
            description = self.soup.find("meta", {"name": "description"})
            return description["content"] if description else None

    def language(self):
        return super().language()
