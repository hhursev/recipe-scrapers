from ._abstract import AbstractScraper


class SaltPepperSkillet(AbstractScraper):
    @classmethod
    def host(cls):
        return "saltpepperskillet.com"

    def author(self):
        author_name = self.schema.author()
        return author_name.capitalize()


    def description(self):
        return self.schema.description()
