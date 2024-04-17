# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class Inspiralized(AbstractScraper):
    @classmethod
    def host(cls):
        return "inspiralized.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()
