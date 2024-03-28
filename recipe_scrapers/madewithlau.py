# mypy: disallow_untyped_defs=False
import re

from ._abstract import AbstractScraper
from ._utils import normalize_string


class MadeWithLau(AbstractScraper):
    @classmethod
    def host(cls):
        return "madewithlau.com"

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
