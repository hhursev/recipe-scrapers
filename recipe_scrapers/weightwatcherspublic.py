# mypy: allow-untyped-defs

from ._utils import get_minutes, get_yields
from .weightwatchers import Weightwatchers


class weightwatchersPublic(Weightwatchers):
    @classmethod
    def host(cls):
        return "www.weightwatchers.com"

    def __findDataContainer(self):
        return self.soup.find("div", {"class": "HorizontalList_list__GESs0"})

    def __extractItemField(self, item):
        return item.find("div", {"data-e2e-name": "attribute_item_value"})

    def total_time(self):
        return get_minutes(
            self.__extractItemField(self.__findDataContainer().contents[0])
        )

    def cook_time(self):
        return get_minutes(
            self.__extractItemField(self.__findDataContainer().contents[2])
        )

    def prep_time(self):
        return get_minutes(
            self.__extractItemField(self.__findDataContainer().contents[1])
        )

    def yields(self):
        return get_yields(
            self.__extractItemField(self.__findDataContainer().contents[3])
        )

    def difficulty(self):
        return self.__extractItemField(
            self.__findDataContainer().contents[4]
        ).get_text()
