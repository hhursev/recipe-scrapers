# mypy: allow-untyped-defs


from ._abstract import AbstractScraper


class EatingWell(AbstractScraper):
    @classmethod
    def host(cls):
        return "eatingwell.com"

    def title(self):
        return self.schema.title()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()
