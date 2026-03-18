from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class StacyLing(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "stacyling.com"
