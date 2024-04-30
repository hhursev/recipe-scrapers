from ._abstract import AbstractScraper


class SaltPepperSkillet(AbstractScraper):
    @classmethod
    def host(cls):
        return "saltpepperskillet.com"

    def author(self):
        return self.schema.author().title()
