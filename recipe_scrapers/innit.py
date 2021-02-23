from typing import Any, Dict, List, Optional

from ._abstract import AbstractScraper

"""
    Note that innit hosts recipes for several companies.  I found it while looking at centralmarket.com
"""


class Innit(AbstractScraper):
    @classmethod
    def host(self, domain="com"):
        return f"innit.{domain}"

    def title(self) -> Optional[str]:
        return self.schema.title()

    def total_time(self) -> Optional[int]:
        return self.schema.total_time()

    def yields(self) -> Optional[str]:
        return self.schema.yields()

    def image(self) -> Optional[str]:
        return self.schema.image()

    def ingredients(self) -> Optional[List[str]]:
        return self.schema.ingredients()

    def instructions(self) -> Optional[str]:
        return self.schema.instructions()

    def ratings(self) -> Optional[float]:
        return self.schema.ratings()

    def nutrients(self) -> Optional[Dict[str, Any]]:
        return self.schema.nutrients()
