from ._abstract import AbstractScraper


class SteamyKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "steamykitchen.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        # Recipe section and schema have no image so stealing from the page
        return self.soup.find("img")["src"]

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        # Schema has no ratings and I can't see any near the recipe
        return None
