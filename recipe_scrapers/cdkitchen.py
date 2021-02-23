from typing import List, Optional

from ._abstract import AbstractScraper


class CdKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "cdkitchen.com"

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

    def image(self) -> Optional[str]:
        return self.schema.image()
