from ._abstract import AbstractScraper


class AnItalianInMyKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "anitalianinmykitchen.com"
