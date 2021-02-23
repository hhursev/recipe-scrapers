from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class TwoPeasAndTheirPod(AbstractScraper):
    @classmethod
    def host(cls):
        return "twopeasandtheirpod.com"

    def title(self) -> Optional[str]:
        return self.soup.find("h2", {"class": "wprm-recipe-name"}).get_text()

    def total_time(self) -> Optional[int]:
        minutes = self.soup.select_one(".wprm-recipe-total_time").get_text()
        unit = self.soup.select_one(".wprm-recipe-total_time-unit").get_text()

        return get_minutes("{} {}".format(minutes, unit))

    def yields(self) -> Optional[str]:
        return get_yields(
            self.soup.select_one(
                "div.wprm-recipe-details-container dl:nth-of-type(5) dd"
            ).get_text()
        )

    def ingredients(self) -> Optional[List[str]]:
        ingredients = self.soup.findAll("li", {"class": "wprm-recipe-ingredient"})

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self) -> Optional[str]:
        instructions = self.soup.select(".wprm-recipe-instruction-text")

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    def image(self) -> Optional[str]:
        image = self.soup.find("div", {"class": "wprm-recipe-image"}).find("img")

        return image["src"] if image else None
