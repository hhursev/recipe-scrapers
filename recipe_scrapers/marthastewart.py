# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class MarthaStewart(AbstractScraper):
    @classmethod
    def host(cls):
        return "marthastewart.com"

    def title(self):
        return self.schema.title()

    def yields(self):
        time_label = self.soup.find("div", string="Total Time:")
        if time_label:
            servings_value = time_label.find_next(
                "div", {"class": "mntl-recipe-details__value"}
            )
            if servings_value:
                return servings_value.text.strip()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()
