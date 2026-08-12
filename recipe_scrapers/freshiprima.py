from ._abstract import AbstractScraper
from ._utils import get_yields


class FreshiPrima(AbstractScraper):
    @classmethod
    def host(cls):
        return "fresh.iprima.cz"

    def yields(self):
        element = self.soup.select_one(
            ".recipe-main-points-molecule .main-point:has(.i-person)"
        )
        return get_yields(element)
