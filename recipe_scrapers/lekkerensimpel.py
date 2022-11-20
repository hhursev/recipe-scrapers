# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._utils import normalize_string


class LekkerEnSimpel(AbstractScraper):
    @classmethod
    def host(cls):
        return "lekkerensimpel.com"

    def author(self):
        return self.schema.author()

    def title(self):
        title = self.soup.find("h1", {"class": "hero__title"}).text
        return normalize_string(title)

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        image = self.soup.find("meta", {"property", "og:image"})
        return image["content"] if image else None

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

    def language(self):
        return "nl-NL"
