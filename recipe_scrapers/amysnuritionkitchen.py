from ._abstract import AbstractScraper


class AmysNuritionKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "amysnutritionkitchen.com"
