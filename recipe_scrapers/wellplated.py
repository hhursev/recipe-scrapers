# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class WellPlated(AbstractScraper):
    @classmethod
    def host(cls):
        return "wellplated.com"

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
        instructions = self.schema.instructions()
        if isinstance(instructions, list):
            instructions = "\n".join(instructions)
        return instructions

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine().replace(",", ", ")

    def description(self):
        return self.schema.description()
