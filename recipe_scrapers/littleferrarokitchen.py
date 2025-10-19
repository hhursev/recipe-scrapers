from ._abstract import AbstractScraper


class LittleFerraroKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "littleferrarokitchen.com"
