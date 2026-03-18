from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class MellisaKNorris(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "melissaknorris.com"
