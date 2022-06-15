from ._abstract import AbstractScraper


class ThePioneerWoman(AbstractScraper):
    @classmethod
    def host(cls):
        return "thepioneerwoman.com"

    def title(self):
        return self.schema.title()

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

    def category(self):
        return self.schema.category()

    def cook_time(self):
        return self.schema.cook_time()

    def prep_time(self):
        return self.schema.prep_time()

    def ratings(self):
        return self.schema.ratings()

    def author(self):
        return self.schema.author()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
