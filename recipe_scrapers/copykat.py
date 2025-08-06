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
