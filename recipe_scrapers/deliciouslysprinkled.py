from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class DeliciouslySprinkled(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "deliciouslysprinkled.com"
