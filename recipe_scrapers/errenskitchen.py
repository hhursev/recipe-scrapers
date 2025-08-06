from ._abstract import AbstractScraper


class ErrensKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "errenskitchen.com"
