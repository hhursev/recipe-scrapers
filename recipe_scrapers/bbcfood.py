from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class BBCFood(AbstractScraper):
    @classmethod
    def host(self, domain="com"):
        return f"bbc.{domain}"

    def title(self) -> Optional[str]:
        return normalize_string(self.soup.find("h1").get_text())

    def total_time(self) -> Optional[int]:
        return sum(
            [
                get_minutes(
                    self.soup.find("p", {"class": "recipe-metadata__prep-time"})
                ),
                get_minutes(
                    self.soup.find("p", {"class": "recipe-metadata__cook-time"})
                ),
            ]
        )

    def yields(self) -> Optional[str]:
        return get_yields(self.soup.find("p", {"class": "recipe-metadata__serving"}))

    def author(self) -> Optional[str]:
        container = self.soup.find("div", {"class": "chef__name"})
        if not container:
            return None

        author = container.a
        return author.text if author else None

    def image(self) -> Optional[str]:
        container = self.soup.find(True, {"class": "recipe-media__image"})
        if not container:
            return None

        image = container.parent.find("img", {"src": True})
        return image["src"] if image else None

    def ingredients(self) -> Optional[List[str]]:
        ingredients = self.soup.findAll(
            "li", {"class": "recipe-ingredients__list-item"}
        )

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self) -> Optional[str]:
        instructions = self.soup.findAll(
            "p", {"class": "recipe-method__list-item-text"}
        )

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
