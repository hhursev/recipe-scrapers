# mypy: allow-untyped-defs

import re

from ._abstract import AbstractScraper


class TasteAtlas(AbstractScraper):
    @classmethod
    def host(cls):
        return "tasteatlas.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        clean_text = re.sub("<[^>]*>", "", self.schema.description())
        return clean_text

    def site_name(self):
        return "Taste Atlas"
