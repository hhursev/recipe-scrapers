from ._abstract import AbstractScraper


class LittleSunnyKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "littlesunnykitchen.com"
