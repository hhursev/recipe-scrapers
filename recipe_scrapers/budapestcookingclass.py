from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class BudapestCookingClass(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "budapestcookingclass.com"

    def image(self):
        image = self.soup.select_one(
            ".fusion-text img.wp-image-5808, .fusion-text p img"
        )
        if image:
            return image.get("data-orig-src") or image.get("src")
