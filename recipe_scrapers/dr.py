from typing import List, Optional

from ._abstract import AbstractScraper


class Dr(AbstractScraper):
    @classmethod
    def host(cls):
        return "dr.dk"

    def title(self) -> Optional[str]:
        return self.schema.title()

    def total_time(self) -> Optional[int]:
        return self.schema.total_time()

    def yields(self) -> Optional[str]:
        return self.schema.yields()

    def image(self) -> Optional[str]:
        return self.schema.image()

    def language(self) -> Optional[str]:
        meta_language = self.soup.find(
            "meta",
            attrs={"name": lambda x: x and x.lower() == "language", "content": True},
        )

        return meta_language.get("content")

    def ingredients(self) -> Optional[List[str]]:
        return self.schema.ingredients()

    def instructions(self) -> Optional[str]:
        return self.schema.instructions()
