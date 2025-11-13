from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class FarmToJar(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "farmtojar.com"

    def author(self):
        return self.soup.select_one('meta[name="author"]')["content"]
