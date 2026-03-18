from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class GrandbabyCakes(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "grandbaby-cakes.com"
