from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class IAmAFoodBlog(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "iamafoodblog.com"
