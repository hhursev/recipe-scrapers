from ._abstract import AbstractScraper


class AfricanBites(AbstractScraper):
    @classmethod
    def host(cls, domain="africanbites.com"):
        return domain
