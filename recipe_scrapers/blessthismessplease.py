from ._abstract import AbstractScraper


class BlessThisMessPlease(AbstractScraper):
    @classmethod
    def host(cls):
        return "blessthismessplease.com"
