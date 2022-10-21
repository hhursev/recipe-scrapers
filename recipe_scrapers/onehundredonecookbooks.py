# mypy: allow-untyped-defs

import re

from ._abstract import AbstractScraper
from ._decorators import opengraph_fallback


class OneHundredOneCookBooks(AbstractScraper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.soup = self.soup.find("div", id="recipe")

    @classmethod
    def host(cls):
        return "101cookbooks.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.soup.find("h1").get_text()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        data = self.soup.find_all("p", limit=3, recursive=False)[-1].get_text()
        extraction = re.search("([0-9]+) servings", data)
        return extraction.group(1) if extraction else None

    @opengraph_fallback
    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredients = self.soup.find("blockquote").p.stripped_strings
        return list(ingredients)

    def instructions(self):
        return self.soup.find_all("p", limit=2, recursive=False)[1].get_text(
            "\n", strip=True
        )

    def ratings(self):
        return None
