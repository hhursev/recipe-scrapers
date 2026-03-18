from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class MomsWithCrockPots(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "momswithcrockpots.com"
