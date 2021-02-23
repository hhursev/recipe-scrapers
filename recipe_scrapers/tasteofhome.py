from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import normalize_string


class TasteOfHome(AbstractScraper):
    @classmethod
    def host(cls):
        return "tasteofhome.com"

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
        instructions = self.soup.findAll("li", {"class": "recipe-directions__item"})
        if instructions:
            return "\n".join(
                [
                    normalize_string(instruction.get_text())
                    for instruction in instructions
                ]
            )
        else:
            # In case our HTML parsing doesn't find any instructions, fall back to what the schema provides.
            return self.schema.instructions()

    def ratings(self) -> Optional[float]:
        return self.schema.ratings()
