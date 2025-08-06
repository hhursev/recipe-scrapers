from ._abstract import AbstractScraper


class WholeFoods(AbstractScraper):
    @classmethod
    def host(cls, domain="com"):
        return f"wholefoodsmarket.{domain}"
