# southernliving.com scraper
# Written by G.D. Wallters
# Freely released the code to recipe_scraper group
# 9 February, 2020
# =======================================================


from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class SouthernLiving(AbstractScraper):
    @classmethod
    def host(cls):
        return "southernliving.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return get_minutes(self.schema.total_time())

    def yields(self):
        return get_yields(self.schema.yields())

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        instructions = self.soup.find("ul", {"class": "instructions-section"}).findAll(
            "li", {"class": "instructions-section-item"}
        )
        return "\n".join(
            [
                normalize_string(
                    instruction.find("div", {"class": "paragraph"}).get_text()
                )
                for instruction in instructions
            ]
        )

    def ratings(self):
        return self.schema.ratings()

    def description(self):
        des = self.soup.find(
            "div",
            attrs={"class": lambda e: e.startswith("recipe-summary") if e else False},
        )
        return normalize_string(des.get_text())
