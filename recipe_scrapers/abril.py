from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import normalize_string


class Abril(AbstractScraper):
    @classmethod
    def host(cls):
        return "claudia.abril.com.br"

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
        return normalize_string(self.schema.instructions())
