from ._abstract import AbstractScraper
from ._exceptions import FieldNotProvidedByWebsiteException


class PostPunkKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "theppk.com"

    def total_time(self):
        raise FieldNotProvidedByWebsiteException(return_value=None)
