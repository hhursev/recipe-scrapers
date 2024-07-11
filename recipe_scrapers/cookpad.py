from ._abstract import AbstractScraper
from ._exceptions import StaticValueException


class CookPad(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookpad.com"

    def site_name(cls):
        raise StaticValueException(return_value="Cookpad")
