# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class ChefSavvy(AbstractScraper):
    @classmethod
    def host(cls):
        return "chefsavvy.com"


    def description(self):
        return self.schema.description()
