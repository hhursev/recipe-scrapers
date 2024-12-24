from ._abstract import AbstractScraper
from ._utils import get_yields, normalize_string


class FoodAndWine(AbstractScraper):
    @classmethod
    def host(cls):
        return "foodandwine.com"

    def yields(self):
        yield_label = self.soup.find(
            "div", {"class": "mntl-recipe-details__label"}, string="Yield:"
        )
        if yield_label:
            yield_value = yield_label.find_next(
                "div", {"class": "mntl-recipe-details__value"}
            )
            if yield_value:
                return get_yields(normalize_string(yield_value.text))
