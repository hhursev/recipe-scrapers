from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class CreativeCanning(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "creativecanning.com"
