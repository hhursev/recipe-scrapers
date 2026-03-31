from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class JoCooks(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "jocooks.com"
