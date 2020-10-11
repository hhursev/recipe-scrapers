from ._abstract import AbstractScraper


class WholeFoods(AbstractScraper):
    @classmethod
    def host(self, domain="com"):
        return f"www.wholefoodsmarket.{domain}"
