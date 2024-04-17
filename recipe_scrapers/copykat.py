# mypy: disallow_untyped_defs=False
# copykat.py
# Written by G.D. Wallters
# Freely released the code to recipe_scraper group
# 8 February, 2020
# =======================================================


from ._abstract import AbstractScraper


class CopyKat(AbstractScraper):
    @classmethod
    def host(cls):
        return "copykat.com"

    def yields(self):
        return self.schema.yields()

    def ratings(self):
        return self.schema.ratings()

    def description(self):
        return self.schema.description()
