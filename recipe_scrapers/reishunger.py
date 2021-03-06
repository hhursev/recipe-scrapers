from ._abstract import AbstractScraper
from ._utils import normalize_string


class Reishunger(AbstractScraper):
    @classmethod
    def host(cls):
        return "reishunger.de"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        # For some reason it uses a dict with index: ingredient
        # values instead of a list
        data = self.schema.data.get("recipeIngredient")
        return [normalize_string(v) for v in data.values()]

    def instructions(self):
        result = self.soup.find("section", {"class": "recipe-preparation"})
        if result:
            result = "\n".join(
                normalize_string(i.get_text()) for i in result.findAll("p")
            )
        return result

    def ratings(self):
        # I cannot see a rating on the page.
        return None
