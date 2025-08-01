from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class MealPrepManual(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "mealprepmanual.com"
