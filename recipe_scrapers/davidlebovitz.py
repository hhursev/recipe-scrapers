from ._abstract import AbstractScraper
from ._exceptions import FieldNotProvidedByWebsiteException


class DavidLebovitz(AbstractScraper):
    @classmethod
    def host(cls):
        return "davidlebovitz.com"

    def total_time(self):
        raise FieldNotProvidedByWebsiteException(return_value=None)
