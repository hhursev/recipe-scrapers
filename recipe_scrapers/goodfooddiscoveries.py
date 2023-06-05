# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class GoodFoodDiscoveries(AbstractScraper):
    @classmethod
    def host(cls):
        return "goodfooddiscoveries.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def prep_time(self):
        return self.schema.prep_time()

    def cook_time(self):
        return self.schema.cook_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        # removing "u003cbu003e" and "u003c/bu003e" as it looks to be used at times to bold text on the site
        return [
            ingredient.replace("u003cbu003e", "").replace("u003c/bu003e", "")
            for ingredient in self.schema.ingredients()
        ]

    def instructions(self):
        return self.schema.instructions()

    def description(self):
        return self.soup.find("p", {"class": "recipe-card-summary"}).get_text()
