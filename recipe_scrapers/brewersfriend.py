from ._abstract import AbstractScraper
from ._exceptions import FieldNotProvidedByWebsiteException


class BrewersFriend(AbstractScraper):
    @classmethod
    def host(cls):
        return "brewersfriend.com"

    def description(self):
        raise FieldNotProvidedByWebsiteException(return_value=None)
