# mypy: allow-untyped-defs

# from pprint import pprint
from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import normalize_string


class JoshuaWeissman(AbstractScraper):
    @classmethod
    def host(cls):
        return "joshuaweissman.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        raise NotImplementedError()

    def yields(self):
        raise NotImplementedError()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredients = [
            li.get_text() for ul in self.soup.findAll("ul") for li in ul.findAll("li")
        ]

        ingredients = [
            normalize_string(ingredient) for ingredient in ingredients if ingredient
        ]

        return ingredients

    def ingredient_groups(self):
        # This is the css for it but web site has weird structuring so it doesn't work properly
        return group_ingredients(
            self.ingredients(),
            self.soup,
            'span[style="font-weight:700"]',
            "ul>li",
        )

    def instructions(self):
        instructions = [
            li.get_text() for ol in self.soup.findAll("ol") for li in ol.findAll("li")
        ]

        instructions = [
            normalize_string(instruction) for instruction in instructions if instruction
        ]

        return "\n".join(instructions)

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.soup.find(id="viewer-foo").get_text()
