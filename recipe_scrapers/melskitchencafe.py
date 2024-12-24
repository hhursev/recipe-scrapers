from ._abstract import AbstractScraper


class MelsKitchenCafe(AbstractScraper):
    @classmethod
    def host(cls):
        return "melskitchencafe.com"
