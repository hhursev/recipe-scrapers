from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class TheKitchenCommunity(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "thekitchencommunity.org"
