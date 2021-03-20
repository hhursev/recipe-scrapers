from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes


class MarthaStewart(AbstractScraper):
    @classmethod
    def host(cls):
        return "marthastewart.com"

    def title(self) -> Optional[str]:
        return self.schema.title()

    def total_time(self) -> Optional[int]:
        s = (
            self.soup.findAll("div", {"class": "two-subcol-content-wrapper"})[0]
            .find("div", {"class": "recipe-meta-item-body"})
            .text.strip()
        )
        return get_minutes(s)

    def yields(self) -> Optional[str]:
        return (
            self.soup.findAll("div", {"class": "two-subcol-content-wrapper"})[1]
            .find("div", {"class": "recipe-meta-item-body"})
            .text.strip()
        )

    def ingredients(self) -> Optional[List[str]]:
        return self.schema.ingredients()

    def instructions(self) -> Optional[str]:
        return self.schema.instructions()

    def ratings(self) -> Optional[float]:
        return self.schema.ratings()
