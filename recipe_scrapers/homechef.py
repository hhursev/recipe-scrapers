# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._decorators import opengraph_fallback


class HomeChef(AbstractScraper):
    @classmethod
    def host(cls):
        return "homechef.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    @opengraph_fallback
    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return "\n".join(
            [
                element.get("name") + "\n\n" + element.get("description")
                for element in self.schema.data.get("recipeInstructions").get(
                    "itemListElement"
                )
            ]
        )

    def description(self):
        return self.schema.description()
