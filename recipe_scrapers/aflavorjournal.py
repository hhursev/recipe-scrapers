from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class AFlavorJournal(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "aflavorjournal.com"
