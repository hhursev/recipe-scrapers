from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class PopSugar(AbstractScraper):
    @classmethod
    def host(cls):
        return "popsugar.com"

    def title(self) -> Optional[str]:
        title = self._context().find("h2", {"class": "recipe-title"}).get_text()
        return normalize_string(title)

    def total_time(self) -> Optional[int]:
        anchor = self._context().find(text="Total Time")
        time = anchor.parent.findNext("dd").get_text()
        return get_minutes(time)

    def yields(self) -> Optional[str]:
        anchor = self._context().find(text="Yield")
        serves = anchor.parent.findNext("dd").get_text()
        return get_yields(serves)

    def image(self) -> Optional[str]:
        article = self.soup.find("article")
        if article:
            return article["data-share-image"]

    def ingredients(self) -> Optional[List[str]]:
        container = self._context().find("h3", text="Ingredients").parent
        entries = container.findAll("li")

        ingredients = []
        skipNext = False
        for entry in entries:
            for item in entry.contents:
                if skipNext:
                    skipNext = False
                    continue

                # Each item is an ingredient entry unless it is a tag. The tags are filtered from the ingredient
                # list. If the tag is a <b> tag the next item is also ignored in order to skip headings.
                if item.name is not None:
                    skipNext = item.name == "b"
                    continue

                ingredients.append(normalize_string(item))

        return ingredients

    def instructions(self) -> Optional[str]:
        container = self._context().find("h3", text="Directions").parent
        return "\n".join([entry.get_text() for entry in container.findAll("li")])

    def _context(self):
        return self.soup.find("div", {"class": "recipe-card"})
