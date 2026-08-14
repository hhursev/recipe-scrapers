from ._abstract import AbstractScraper
from ._utils import get_yields
from ._grouping_utils import group_ingredients


class FreshiPrima(AbstractScraper):
    @classmethod
    def host(cls):
        return "fresh.iprima.cz"

    def yields(self):
        element = self.soup.select_one(
            ".recipe-main-points-molecule .main-point:has(.i-person)"
        )
        return get_yields(element)

    def ingredient_groups(self):
        if len(self.soup.select(".ingredients-box")) <= 1:
            return super().ingredient_groups()

        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".ingredients-box h3",
            ".ingredients-box li",
        )
