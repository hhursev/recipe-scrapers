# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._utils import normalize_string


class SimplyRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "simplyrecipes.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        steps = self.soup.find(
            "div", {"class": "structured-project__steps"}
        ).ol.findAll("li")

        return "\n".join(
            [
                normalize_string(
                    step.div.text + "".join([p.text for p in step.findAll("p")])
                )
                for step in steps
            ]
        )
