from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class KrollsKorner(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "krollskorner.com"

    def author(self):
        author_tag = self.soup.select_one(
            ".wprm-recipe-details.wprm-recipe-author.wprm-block-text-normal a"
        )
        return author_tag.get_text(strip=True)
