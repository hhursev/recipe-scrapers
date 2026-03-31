from ._abstract import AbstractScraper
from ._exceptions import StaticValueException


class TheVintageMixer(AbstractScraper):
    @classmethod
    def host(cls):
        return "thevintagemixer.com"

    def site_name(self):
        raise StaticValueException(return_value="Vintage Mixer")
