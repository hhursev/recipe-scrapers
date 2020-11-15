from ._abstract import AbstractScraper


class BonAppetit(AbstractScraper):
    @classmethod
    def host(cls):
        return "bonappetit.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return 0

    def yields(self):
        return self.schema.yields()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()
