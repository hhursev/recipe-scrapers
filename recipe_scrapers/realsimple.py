# mypy: disallow_untyped_defs=False
import re

from ._abstract import AbstractScraper
from ._utils import get_yields


class RealSimple(AbstractScraper):
    @classmethod
    def host(cls):
        return "realsimple.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return get_yields(
            self.soup.find("div", string=re.compile(r"Yield:")).parent.get_text()
        )

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()
