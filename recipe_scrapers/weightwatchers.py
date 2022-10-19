# mypy: allow-untyped-defs

import re

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class Weightwatchers(AbstractScraper):
    @classmethod
    def host(cls):
        return "www.weightwatchers.com"

    def author(self):
        return "WeightWatchers"

    def title(self):
        return self.soup.find("h1").get_text().strip()

    def category(self):
        return "WeightWatchers"

    # cooking times, yield, difficulty are in a common div in public and non-public recipes
    # but class of that block and sub elements are different
    # so finding the block and extracting a value will be overridden in class for public recipes,
    # but picking the data item based on order is don in this base class (total_time(), cook_time() and so on)
    def _findDataContainer(self):
        return self.soup.find("div", {"class": "styles_container__3N3E8"})

    def _extractItemField(self, item):
        return item.contents[1]

    def total_time(self):
        return get_minutes(
            self._extractItemField(self._findDataContainer().contents[0])
        )

    def prep_time(self):
        return get_minutes(
            self._extractItemField(self._findDataContainer().contents[1])
        )

    def cook_time(self):
        return get_minutes(
            self._extractItemField(self._findDataContainer().contents[2])
        )

    def yields(self):
        return get_yields(self._extractItemField(self._findDataContainer().contents[3]))

    def difficulty(self):
        return self._extractItemField(self._findDataContainer().contents[4]).get_text()

    #   Alternative way to extract data based on description instead of position
    #    def total_time(self):
    #        return get_minutes(
    #            self.__findDataContainer()
    #            .find("div", string=re.compile(r"minutes Total Time"))
    #            .previous_sibling
    #        )

    def image(self):
        backgroundImgStyle = self.soup.find("div", {"class": "styles_image__2dnNm"})[
            "style"
        ]

        if backgroundImgStyle:
            return (
                re.compile(r'url\("(?P<imgurl>\S*)"\);')
                .search(backgroundImgStyle)
                .groupdict()
                .get("imgurl")
            )

        return None

    def __parseIngridient(self, ingridient):
        ingridientName = normalize_string(
            ingridient.find("div", {"class": "styles_ingredientName__1Vffd"})
            .find("div")
            .get_text()
        )
        portionParts = ingridient.find(
            "div", {"class": "styles_portion__2NQyq"}
        ).find_all("span")
        amount = (
            normalize_string(portionParts[0].get_text())
            + " "
            + normalize_string(portionParts[1].get_text())
        )

        if portionParts[2].get_text():
            ingridientName += "; " + normalize_string(
                portionParts[2].get_text()
            ).replace(", ", "")

        return amount + " " + ingridientName

    def ingredients(self):
        result = []
        ingridients = self.soup.find(
            "h3", {"id": "food-detail-recipe-ingredients-header"}
        ).parent.find_all("div", {"class": "styles_name__1OYVU"})
        for ingridient in ingridients:
            result.append(self.__parseIngridient(ingridient))
        return result

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

    def nutrients(self):
        result = (
            self.soup.find(
                "img", {"class": "styles_positivePointsIcon__2XYyV"}
            ).next_sibling.get_text()
            + " personal points"
        )
        veggiepoints = self.soup.find(
            "div", {"class": "styles_vegetableServings__2YSPy"}
        )
        if veggiepoints:
            result += "\n" + normalize_string(
                veggiepoints.find(
                    "div", {"class": "styles_container__2p-YG"}
                ).next_sibling.get_text()
            )

        return result
