import re

from ._abstract import AbstractScraper
from ._utils import normalize_string


class MadeWithLau(AbstractScraper):
    @classmethod
    def host(cls):
        return "madewithlau.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def description(self):
        return self.schema.description()

    def cook_time(self):
        return self.schema.cook_time()

    def prep_time(self):
        return self.schema.prep_time()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        # collect headers
        headers = [
            header.find("h4")
            for header in self.soup.findAll(
                "div",
                {"class", re.compile("summary-step_step-label.*")},
            )
        ]

        # collect steps associated with each header
        step_sets = self.soup.findAll(
            "div",
            {"class", re.compile("summary-step_step__.*")},
        )

        # merge headers and steps
        instructions = [
            p
            for pair in zip(headers, step_sets)
            for p in [
                pair[0],
                *(pair[1].find("div") or pair[1]),
            ]
        ]

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    def cuisine(self):
        return self.schema.cuisine()

    def category(self):
        return self.schema.category()
