# mypy: allow-untyped-defs


from ._abstract import AbstractScraper


class EatingWell(AbstractScraper):
    @classmethod
    def host(cls):
        return "eatingwell.com"

    def yields(self):
        return self.schema.yields()
