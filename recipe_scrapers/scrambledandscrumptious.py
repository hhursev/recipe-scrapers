from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class ScrambledAndScrumptious(AbstractScraper):
    @classmethod
    def host(cls):
        return "scrambledandscrumptious.com"

    def ingredients(self):
        return [
            li.get_text(strip=True)
            for li in self.soup.select("div._33 ul[role='list'] li")
        ]

    def instructions(self):
        return "\n".join(
            [
                li.get_text(strip=True)
                for li in self.soup.select("div._66 ol[role='list'] li")
            ]
        )

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "div._33 p",
            "div._33 ul[role='list'] li",
        )
