# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class Drinkoteket(AbstractScraper):
    @classmethod
    def host(cls):
        return "drinkoteket.se"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return 1

    def image(self):
        return self.schema.image()

    def ingredients(self):
        # return self.schema.ingredients()
        _ingredients = (
            self.soup.find("ul", {"class": "ingredients"}).find_all("span").copy()
        )
        return [
            " ".join([x.strip() for x in i.getText().split("\n") if x.strip() != ""])
            for i in _ingredients
            if len(i) != 1
        ]

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
