# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._utils import normalize_string


class Maangchi(AbstractScraper):
    @classmethod
    def host(cls):
        return "maangchi.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        before = self.soup.find("h2", string="Ingredients").find_all_next("li")
        after = self.soup.find("h2", string="Directions").find_all_previous("li")
        list_before = [normalize_string(b.get_text()) for b in before]
        list_after = [normalize_string(a.get_text()) for a in after]
        return [x for x in list_before if x in list_after]

    def instructions(self):
        ols = self.soup.find("div", {"class": "entry"}).find_all("ol")
        instructions = []
        for ol in ols:
            for li in ol.findAll("li"):
                instructions.append(li)
        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
