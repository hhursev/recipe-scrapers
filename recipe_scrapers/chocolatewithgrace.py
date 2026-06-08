from ._abstract import AbstractScraper
from ._exceptions import StaticValueException


class ChocolateWithGrace(AbstractScraper):
    @classmethod
    def host(cls):
        return "chocolatewithgrace.com"

    def site_name(self):
        raise StaticValueException(return_value="Chocolate with Grace")
