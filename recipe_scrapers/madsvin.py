# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class Madsvin(AbstractScraper):
    @classmethod
    def host(cls):
        return "madsvin.com"

    def description(self):
        return self.schema.description()
