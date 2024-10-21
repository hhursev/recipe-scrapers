from ._abstract import AbstractScraper
from ._exceptions import StaticValueException


class TheKitchn(AbstractScraper):
    @classmethod
    def host(cls):
        return "thekitchn.com"

    def site_name(self):
        raise StaticValueException(return_value="The Kitchn")
