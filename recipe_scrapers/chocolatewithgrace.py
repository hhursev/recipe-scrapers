from ._abstract import AbstractScraper


class ChocolateWithGrace(AbstractScraper):
    @classmethod
    def host(cls):
        return "chocolatewithgrace.com"
