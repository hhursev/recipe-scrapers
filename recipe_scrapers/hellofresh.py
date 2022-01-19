from ._abstract import AbstractScraper


class HelloFresh(AbstractScraper):
    @classmethod
    def host(self, domain="com"):
        return f"hellofresh.{domain}"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def image(self):
        return self.schema.image()

    def nutrients(self):
        return self.schema.nutrients()

    def cuisine(self):
        return self.schema.cuisine()

    def category(self):
        return self.schema.category()
