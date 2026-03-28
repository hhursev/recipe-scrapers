from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class paintthekitchenred(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "paintthekitchenred.com"
    
