# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._decorators import opengraph_fallback, schemaorg_fallback


class Coop(AbstractScraper):
    @classmethod
    def host(cls):
        return "coop.se"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def cook_time(self):
        return self.schema.cook_time()

    @schemaorg_fallback
    def total_time(self):
        pass

    def yields(self):
        return self.schema.yields()

    @opengraph_fallback
    def image(self):
        image = self.schema.image()
        if image is None or image == "":
            image = self.schema.data.get("image")
            if (
                image
                and isinstance(image, list)
                and len(image) >= 1
                and isinstance(image[0], str)
                and image[0].startswith("//")
            ):
                image = "https:" + image[0]
        return image

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
