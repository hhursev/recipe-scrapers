from typing import List, Optional

from ._abstract import AbstractScraper


class CookEatShare(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookeatshare.com"

    def title(self) -> Optional[str]:
        return self.schema.title()

    def total_time(self) -> Optional[int]:
        return 0

    def image(self) -> Optional[str]:
        return self.schema.image()

    def ingredients(self) -> Optional[List[str]]:
        return self.schema.ingredients()

    def instructions(self) -> Optional[str]:
        return self.schema.instructions()
