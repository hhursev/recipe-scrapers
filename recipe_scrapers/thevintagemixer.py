# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class TheVintageMixer(AbstractScraper):
    @classmethod
    def host(cls):
        return "thevintagemixer.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()
