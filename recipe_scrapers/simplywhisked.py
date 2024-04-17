# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class SimplyWhisked(AbstractScraper):
    @classmethod
    def host(cls):
        return "simplywhisked.com"

    def ratings(self):
        return self.schema.ratings()
