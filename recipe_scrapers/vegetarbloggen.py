# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class Vegetarbloggen(AbstractScraper):
    @classmethod
    def host(cls):
        return "vegetarbloggen.no"

    def instructions(self):
        return self.schema.instructions().strip()
