from typing import List, Optional

from bs4 import BeautifulSoup

from ._abstract import AbstractScraper


class BBCGoodFood(AbstractScraper):
    @classmethod
    def host(cls):
        return "bbcgoodfood.com"

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
        inst = str(self.schema.instructions())
        instSoup = BeautifulSoup(inst, features="html.parser")
        return instSoup.text
