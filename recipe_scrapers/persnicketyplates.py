from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class PersnicketyPlates(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "persnicketyplates.com"
