from ._abstract import AbstractScraper


class SaltPepperSkillet(AbstractScraper):
    @classmethod
    def host(cls):
        return "saltpepperskillet.com"

    def author(self):
        author_name = self.schema.author()
        return author_name.capitalize()

    def category(self):
        return self.schema.category()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
