from ._abstract import AbstractScraper


class FoodNetwork(AbstractScraper):
    @classmethod
    def host(cls, domain="co.uk"):
        return f"foodnetwork.{domain}"
