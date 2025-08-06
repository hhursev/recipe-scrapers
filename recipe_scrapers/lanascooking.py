from ._abstract import AbstractScraper


class LanasCooking(AbstractScraper):
    @classmethod
    def host(cls):
        return "lanascooking.com"
