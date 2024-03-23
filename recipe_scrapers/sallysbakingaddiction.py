# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class SallysBakingAddiction(AbstractScraper):
    @classmethod
    def host(cls):
        return "sallysbakingaddiction.com"
