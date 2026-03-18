from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class SugarSpunRun(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "sugarspunrun.com"
