# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._exceptions import RecipeScrapersExceptions


class DavidLebovitz(AbstractScraper):
    @classmethod
    def host(cls):
        return "davidlebovitz.com"

    def total_time(self):
        raise RecipeScrapersExceptions(
            f"{self.host()} does not provide time information."
        )
