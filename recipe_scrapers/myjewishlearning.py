# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class MyJewishLearning(AbstractScraper):
    @classmethod
    def host(cls):
        return "myjewishlearning.com"

    def category(self):
        return self.schema.category()
