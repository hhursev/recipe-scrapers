from ._abstract import AbstractScraper


class Eatsmarter(AbstractScraper):
    @classmethod
    def host(cls, domain="com"):
        return f"eatsmarter.{domain}"
