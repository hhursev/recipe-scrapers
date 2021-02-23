from typing import List, Optional

from ._abstract import AbstractScraper


class BudgetBytes(AbstractScraper):
    @classmethod
    def host(cls):
        return "budgetbytes.com"

    def title(self) -> Optional[str]:
        return self.schema.title()

    def total_time(self) -> Optional[int]:
        return self.schema.total_time()

    def yields(self) -> Optional[str]:
        return self.schema.yields()

    def ingredients(self) -> Optional[List[str]]:
        return self.schema.ingredients()

    def instructions(self) -> Optional[str]:
        return self.schema.instructions()

    def ratings(self) -> Optional[float]:
        return self.schema.ratings()
