from ._abstract import AbstractScraper


class ItDoesntTasteLikeChicken(AbstractScraper):
    @classmethod
    def host(cls):
        return "itdoesnttastelikechicken.com"
