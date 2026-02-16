from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class honest_food(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "honest-food.net"
    
