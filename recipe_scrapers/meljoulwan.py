import re

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields
from ._exceptions import StaticValueException
from ._grouping_utils import group_ingredients


class Meljoulwan(AbstractScraper):
    @classmethod
    def host(cls):
        return "meljoulwan.com"

    def author(self):
        return (
            self.soup.find("div", {"class": "post-author"})
            .find("span")
            .get_text()
            .strip()
        )

    def title(self):
        return self.soup.find("title").get_text().strip()

    def category(self):
        ul_list = (
            self.soup.find("div", {"class": "post-info"})
            .find("div", {"class", "post-category"})
            .find_all("a")
        )

        categories = []
        for li in ul_list:
            if li.get_text() != "Blog":
                categories.append(li.get_text())
        return ",".join(categories)

    def _extract_info(self, pattern):
        infostring = self.soup.find("div", {"class": "recipe-copy"}).get_text().strip()
        matches = re.search(pattern, infostring)
        return matches.group(1)

    def total_time(self):
        time = self._extract_info(r"Total time\s*:?\s*(\d+)\s*(?:minutes|min)")
        if not time:
            prep_time = self.prep_time()
            cook_time = self.cook_time()
            if prep_time or cook_time:
                time = (prep_time or 0) + (cook_time or 0)
        return get_minutes(time)

    def prep_time(self):
        time = self._extract_info(r"Prep\s*:?\s*(\d+)\s*(?:minutes|min)")
        return get_minutes(time)

    def cook_time(self):
        time = self._extract_info(r"Cook\s*:?\s*(\d+)\s*(?:minutes|min)")
        return get_minutes(time)

    def yields(self):
        yield_value = self._extract_info(r"Serves\s(\d+)")
        if yield_value:
            return get_yields(yield_value)

        # Check for the alternative format
        yield_value = self._extract_info(
            r"Serves\s(\d+)\s*\|\s*Total time\s*:?\s*\d+\s*minutes\s*\|"
        )
        return get_yields(yield_value)

    def ingredients(self):
        ul_list = self.soup.find("div", {"class": "tabbed-list"}).find_all("ul")

        ingredients = []
        for ul in ul_list:
            li_list = ul.find_all("li")
            for li in li_list:
                ingredients.append(li.get_text().strip())

        return ingredients

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".tabbed-list h6",
            ".tabbed-list li",
        )

    def instructions(self):
        ul_list = self.soup.find("div", {"class": "numbered-list"}).find_all(
            "div", {"class", "num-list-group"}
        )

        instructions = []
        for li in ul_list:
            instructions.append(
                li.find("div", {"class": "num-list-copy"}).get_text().strip()
            )
        return "\n".join(instructions)

    def language(self):
        raise StaticValueException(return_value="en-US")
