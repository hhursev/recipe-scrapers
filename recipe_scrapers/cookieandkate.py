from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class CookieAndKate(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookieandkate.com"

    def title(self) -> Optional[str]:
        return self.soup.find("h1", {"class": "entry-title"}).get_text()

    def total_time(self) -> Optional[int]:
        return get_minutes(
            self.soup.find("span", {"class": "tasty-recipes-total-time"})
        )

    def yields(self) -> Optional[str]:
        yields = self.soup.find("span", {"class": "tasty-recipes-yield"}).get_text()

        return get_yields("{} servings".format(yields))

    def ingredients(self) -> Optional[List[str]]:
        ingredients = self.soup.find(
            "div", {"class": "tasty-recipe-ingredients"}
        ).find_all("li")

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self) -> Optional[str]:
        instructions = self.soup.find(
            "div", {"class": "tasty-recipe-instructions"}
        ).find_all("li")

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    def ratings(self) -> Optional[float]:
        return round(float(self.soup.find("span", {"class": "average"}).get_text()), 2)
