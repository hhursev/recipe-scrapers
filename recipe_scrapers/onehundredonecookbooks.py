# mypy: disallow_untyped_defs=False
import re

from ._abstract import AbstractScraper


class OneHundredOneCookBooks(AbstractScraper):
    @classmethod
    def host(cls):
        return "101cookbooks.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        container = self.soup.find("div", id="recipe")
        data = container.find_all("p", limit=3, recursive=False)[-1].get_text()
        extraction = re.search("([0-9]+) servings", data)
        return extraction.group(1) if extraction else None

    def image(self):
        return self.schema.image()

    def ingredients(self):
        container = self.soup.find("div", id="recipe")
        ingredients = container.find("blockquote").p.stripped_strings
        return list(ingredients)

    def instructions(self):
        container = self.soup.find("div", id="recipe")
        return container.find_all("p", limit=2, recursive=False)[1].get_text(
            "\n", strip=True
        )

    def ratings(self):
        return None
