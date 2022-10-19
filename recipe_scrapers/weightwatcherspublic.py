# mypy: allow-untyped-defs

from ._utils import normalize_string
from .weightwatchers import Weightwatchers


# collect the differences between public and non-public weightwatcher recipes in this class
class weightwatchersPublic(Weightwatchers):
    @classmethod
    def host(cls):
        return "www.weightwatchers.com"

    def _findDataContainer(self):
        return self.soup.find("div", {"class": "HorizontalList_list__GESs0"})

    def _extractItemField(self, item):
        return item.find("div", {"data-e2e-name": "attribute_item_value"})

    def image(self):
        return self.soup.find("img", {"class": "FoodMasthead_heroImage__BjVdZ"})["src"]

    def nutrients(self):
        return self.soup.find("div", {"class": "Coin_text__3UOb0"})["aria-label"]

    def description(self):
        return normalize_string(
            self.soup.find("div", {"data-e2e-name": "food_masthead_detail_description"})
            .find("div", {"class": "ReadMoreLess_collapsed__IAzxP"})
            .get_text()
        )
