from ._abstract import AbstractScraper


class FortyAprons(AbstractScraper):
    @classmethod
    def host(cls):
        return "40aprons.com"

    def author(self):
        return self.schema.author()

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

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()

    def cook_time(self):
        return self.schema.cook_time()

    def prep_time(self):
        return self.schema.prep_time()

    def nutrients(self):
        return self.schema.nutrients()

    def keywords(self):
        return self.schema.keywords()

    def ratings(self):
        return "No ratings available"

    def ratings_count(self):
        return "0 (No ratings available)"

    def reviews(self):
        return "No reviews available"

    def equipment(self):
        return "No equipment information available"

    def cooking_method(self):
        return "No cooking method available"

    def dietary_restrictions(self):
        return "No dietary restriction information available"
