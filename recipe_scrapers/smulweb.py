# mypy: allow-untyped-defs

import re

from ._abstract import AbstractScraper


class Smulweb(AbstractScraper):
    instruction_delimiter = re.compile(r"(\.|\))\s*([A-Z])")

    @classmethod
    def host(cls):
        return "smulweb.nl"

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
        schema_instructions = self.schema.instructions()
        return self.instruction_delimiter.sub(r"\1\n\2", schema_instructions)

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
