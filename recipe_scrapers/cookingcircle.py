import re

from ._abstract import AbstractScraper
from ._utils import get_minutes


class CookingCircle(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookingcircle.com"

    def author(self):
        return (
            self.soup.find("div", {"class": "recipe-author"})
            .findChild("span", {"class": "text-uppercase"})
            .get_text()
        )

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        ul = self.soup.find("ul", {"class": "single-method-overview__times"})
        totalTime = None
        for li in ul.find_all("li"):
            if li.span.get_text().lower() == "total time:":
                totalTime = li.span.find_next().get_text()

        if totalTime is not None:
            totalTime = re.findall("[0-9]+", totalTime)[0]
        return get_minutes(totalTime)

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ulList = (
            self.soup.find(
                "div", {"class": "single-ingredients__group", "data-unit": "metric"}
            )
            .findChild("ul", {"class": "single-ingredients__list"})
            .findChildren("li")
        )

        ingredients = []
        for li in ulList:
            ingredients.append(
                li.get_text().replace("\t", "").replace("\n\n", " ").replace("\n", "")
            )
        return ingredients

    def instructions(self):
        ulList = self.soup.find("ul", {"class": "single-method__method"}).findChildren(
            "li"
        )

        instructions = []
        for li in ulList:
            instructions.append(li.get_text().strip().replace("\n", " "))

        return "\n".join(instructions)
