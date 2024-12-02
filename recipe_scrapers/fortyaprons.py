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

    # def ingredient_groups(self):
    #     return self.schema.ingredient_groups()
    
    # def equipment(self):
    #     return self.schema.equipment()
