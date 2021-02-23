from typing import List, Optional

from ._abstract import AbstractScraper


class AtelierDesChefs(AbstractScraper):
    @classmethod
    def host(cls):
        return "atelierdeschefs.fr"

    def title(self) -> Optional[str]:
        return self.schema.title()

    def total_time(self) -> Optional[int]:
        return self.schema.total_time()

    def yields(self) -> Optional[str]:
        yields = self.soup.find("option", {"class": "yield"})
        return f"{yields.get('value')} Servings"

    def ingredients(self) -> Optional[List[str]]:
        return self.schema.ingredients()

    def instructions(self) -> Optional[str]:
        # clean the text : remove trailing newlines, and consecutives newlines
        instructions = self.soup.find(
            "ul", {"class": "recipe-steps arial marginT20"}
        ).text.splitlines()
        return "\n".join(
            [paragraph for paragraph in instructions if len(paragraph) > 0]
        )

    def ratings(self) -> Optional[float]:
        return self.schema.ratings()
