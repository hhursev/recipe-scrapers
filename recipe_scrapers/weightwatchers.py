# mypy: allow-untyped-defs

import re

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class Weightwatchers(AbstractScraper):
    @classmethod
    def host(cls):
        return "weightwatchers.de"

    def author(self):
        return "WeightWatchers"

    def title(self):
        return self.soup.find("h1").get_text().strip()

    def category(self):
        return "WeightWatchers"

    def total_time(self):
        return get_minutes(
            self.soup.find("div", {"class": "styles_container__3N3E8"})
            .find("div", string=re.compile(r"minutes Total Time"))
            .previous_sibling
        )

    def cook_time(self):
        return get_minutes(
            self.soup.find("div", {"class": "styles_container__3N3E8"})
            .find("div", string=re.compile(r"minutes Cook Time"))
            .previous_sibling
        )

    def prep_time(self):
        return get_minutes(
            self.soup.find("div", {"class": "styles_container__3N3E8"})
            .find("div", string=re.compile(r"minutes Preparation Time"))
            .previous_sibling
        )

    def yields(self):
        return get_yields(
            self.soup.find("div", {"class": "styles_container__3N3E8"}).find(
                "div", string=re.compile(r"Serves \d+ people")
            )
        )

    def difficulty(self):
        return (
            self.soup.find("div", {"class": "styles_container__3N3E8"})
            .find("div", string=re.compile(r"Difficulty Level:"))
            .previous_sibling.get_text()
        )

    def image(self):
        backgroundImgStyle = self.soup.find("div", {"class": "styles_image__2dnNm"})[
            "style"
        ]
        return (
            re.compile(r'url\("(?P<imgurl>\S*)"\);')
            .search(backgroundImgStyle)
            .groupdict()
            .get("imgurl")
        )

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        instructions = self.soup.find(
            "h3", {"id": "food-detail-recipe-instruction-header"}
        ).parent.find("ol")
        return "\n".join(
            [
                normalize_string(instruction.get_text())
                for instruction in instructions.find_all("div", {"class": "copy-1"})
            ]
        )

    def description(self):
        return self.soup.find("div", {"class": "copy-1"}).get_text().strip()
