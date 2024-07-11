from ._abstract import AbstractScraper


class CookEatShare(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookeatshare.com"

    def total_time(self):
        return None
