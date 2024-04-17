# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Cybercook(AbstractScraper):
    @classmethod
    def host(cls):
        return "cybercook.com.br"

    def ratings(self):
        return self.schema.ratings()
