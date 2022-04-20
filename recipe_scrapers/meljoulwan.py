import re

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields


class Meljoulwan(AbstractScraper):
    @classmethod
    def host(cls):
        return "meljoulwan.com"

    def author(self):
        return (
            self.soup.find("div", {"class": "post-author"})
            .findChild("span")
            .get_text()
            .strip()
        )

    def title(self):
        return (
            self.soup.find("div", {"class": "recipe-post"})
            .findChild("h2")
            .get_text()
            .strip()
        )

    def category(self):
        ulList = (
            self.soup.find("div", {"class": "post-info"})
            .findChild("div", {"class", "post-category"})
            .findChildren("a")
        )

        categories = []
        for li in ulList:
            if li.get_text() != "Blog":
                categories.append(li.get_text())
        return ",".join(categories)

    def total_time(self):
        infostring = (
            self.soup.find("div", {"class": "recipe-copy"}).find("em").get_text()
        )

        matches = re.search(
            r"(Cook|Total time:)\s(\d+\-?\d+)\s\bmin(utes)?", infostring
        )

        return get_minutes(matches.group(2))

    def yields(self):
        infostring = (
            self.soup.find("div", {"class": "recipe-copy"})
            .find("em")
            .get_text()
            .strip()
        )

        matches = re.search(r"^Serves\s(\d+\-?\–?\d+)", infostring)

        return get_yields(matches.group(1))

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ulList = self.soup.find("div", {"class": "tabbed-list"}).findChildren("ul")

        ingredients = []
        for ul in ulList:
            liList = ul.findChildren("li")
            for li in liList:
                ingredients.append(li.get_text().strip())

        return ingredients

    def instructions(self):
        ulList = self.soup.find("div", {"class": "numbered-list"}).findChildren(
            "div", {"class", "num-list-group"}
        )

        count = 0
        instructions = []
        for li in ulList:
            count += 1
            instructions.append(
                str(count)
                + ". "
                + li.findChild("div", {"class": "num-list-copy"}).get_text().strip()
            )
        return "\n".join(instructions)
