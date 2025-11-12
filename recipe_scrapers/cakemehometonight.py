from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class CakeMeHomeTonight(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "cakemehometonight.com"
