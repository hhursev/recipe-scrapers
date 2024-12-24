from ._abstract import AbstractScraper


class ClosetCooking(AbstractScraper):
    @classmethod
    def host(cls):
        return "closetcooking.com"
