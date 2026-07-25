from ._abstract import AbstractScraper


class CloudyKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "cloudykitchen.com"
