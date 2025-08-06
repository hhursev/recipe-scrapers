from ._abstract import AbstractScraper
from ._exceptions import StaticValueException


class InBloomBakery(AbstractScraper):
    @classmethod
    def host(cls):
        return "inbloombakery.com"

    def site_name(self):
        raise StaticValueException(return_value="In Bloom Bakery")
