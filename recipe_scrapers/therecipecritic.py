# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class Therecipecritic(AbstractScraper):
    @classmethod
    def host(cls):
        return "therecipecritic.com"

    def author(self):
        return "The Recipe Critic"

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
