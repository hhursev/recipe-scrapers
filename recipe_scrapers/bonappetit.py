from typing import List, Optional

from ._abstract import AbstractScraper


class BonAppetit(AbstractScraper):
    @classmethod
    def host(cls):
        return "bonappetit.com"

    def title(self) -> Optional[str]:
        return self.schema.title()

    def total_time(self) -> Optional[int]:
        return 0

    def yields(self) -> Optional[str]:
        return self.schema.yields()

    def ingredients(self) -> Optional[List[str]]:
        return self.schema.ingredients()

    def instructions(self) -> Optional[str]:
        return self.schema.instructions()
