from ._abstract import AbstractScraper
from ._exceptions import StaticValueException


class CookEatShare(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookeatshare.com"

    def site_name(self):
        raise StaticValueException(return_value="CookEatShare Cookbook")

    def total_time(self):
        return None
