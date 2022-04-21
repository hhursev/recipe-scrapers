from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields


class PingoDoce(AbstractScraper):
    @classmethod
    def host(cls):
        return "pingodoce.pt"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return get_minutes(self.soup.findAll("div", {"class": "info"})[0])

    def yields(self):
        return get_yields(self.soup.findAll("div", {"class": "info"})[2])

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        instructions = self.soup.findAll("div", {"class": "step-description"})
        return "\n".join([i.get_text() for i in instructions])

    def ratings(self):
        return self.schema.ratings()

    def description(self):
        return self.schema.description()
