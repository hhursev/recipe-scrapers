# mypy: disallow_untyped_defs=False
import re

from ._abstract import AbstractScraper
from ._utils import normalize_string


class AlbertHeijn(AbstractScraper):
    @classmethod
    def host(cls):
        return "ah.nl"

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

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        instructions = [
            normalize_string(step.get_text())
            # get steps root
            for root in self.soup.findAll(
                "div",
                {"class", re.compile("recipe-preparation-steps_root.*")},
            )
            # get steps
            for step in root.findAll("p")
        ]

        if instructions:
            return "\n".join(instructions)

        # try schema.org
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
