# copykat.py
# Written by G.D. Wallters
# Freely released the code to recipe_scraper group
# 8 February, 2020
# =======================================================


from ._abstract import AbstractScraper
from ._utils import normalize_string


class CopyKat(AbstractScraper):
    @classmethod
    def host(cls):
        return "copykat.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def description(self):
        d = normalize_string(self.soup.find("span", {"style": "display: block;"}).text)

        return d if d else None
