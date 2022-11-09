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
        before = self.soup.find("h4", string="Directions").find_all_previous("li")
        after = self.soup.find("h4", string="Ingredients:").find_all_next("li")
        lstBfr = [normalize_string(b.get_text()) for b in before]
        lstAfr = [normalize_string(a.get_text()) for a in after]
        lstBfr.reverse()
        return [x for x in lstBfr if x in lstAfr]

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
