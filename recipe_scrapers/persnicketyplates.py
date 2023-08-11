# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class PersnicketyPlates(AbstractScraper):
    @classmethod
    def host(cls):
        return "persnicketyplates.com"

    def author(self):
        author_tag = self.soup.find("meta", {"name": "author"})
        return author_tag["content"] if author_tag else "persnicketyplates"

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

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

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
