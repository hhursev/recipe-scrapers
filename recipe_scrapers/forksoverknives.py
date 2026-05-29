from ._abstract import AbstractScraper
from ._utils import get_yields


class ForksOverKnives(AbstractScraper):
    @classmethod
    def host(cls):
        return "forksoverknives.com"

    def author(self):
        return self.soup.select_one('a[href*="/contributors/"]').get_text(strip=True)

    def yields(self):
        yield_str = self.soup.select_one(".add-info li:nth-of-type(2) span").get_text(
            strip=True
        )
        return get_yields(yield_str)
