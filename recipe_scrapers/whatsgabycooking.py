from ._abstract import AbstractScraper


class WhatsGabyCooking(AbstractScraper):
    @classmethod
    def host(cls):
        return "whatsgabycooking.com"
