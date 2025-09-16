from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class BakingSense(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "baking-sense.com"
