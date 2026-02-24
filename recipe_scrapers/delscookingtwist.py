from ._abstract import AbstractScraper


class DelsCookingTwist(AbstractScraper):
    @classmethod
    def host(cls):
        return "delscookingtwist.com"
