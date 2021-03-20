from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class WikiCookbook(AbstractScraper):
    @classmethod
    def host(cls):
        return "en.wikibooks.org"

    def title(self) -> Optional[str]:
        return self.soup.find("h1").get_text().replace("Cookbook:", "")

    def total_time(self) -> Optional[int]:
        return get_minutes(self.soup.find("th", string="Time").find_next_sibling("td"))

    def yields(self) -> Optional[str]:
        return get_yields(
            self.soup.find("th", string="Servings").find_next_sibling("td")
        )

    def image(self) -> Optional[str]:
        image = self.soup.find("a", {"class": "image"}).find("img", {"src": True})
        return image["src"] if image else None

    def ingredients(self) -> Optional[List[str]]:
        ingredients = (
            self.soup.find("span", {"id": "Ingredients"}).find_next("ul").findAll("li")
        )

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self) -> Optional[str]:
        instructions = (
            self.soup.find("span", {"id": "Procedure"}).find_next("ol").findAll("li")
        )

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
