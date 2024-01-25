# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class PingoDoce(AbstractScraper):
    @classmethod
    def host(cls):
        return "pingodoce.pt"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        instructions = self.soup.findAll("div", {"class": "step-description"})
        return "\n".join([i.get_text() for i in instructions])

    def ratings(self):
        return self.schema.ratings()

    def description(self):
        return self.schema.description()
