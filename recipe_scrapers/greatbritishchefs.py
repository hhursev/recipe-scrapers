from ._abstract import AbstractScraper


class GreatBritishChefs(AbstractScraper):
    @classmethod
    def host(cls):
        return "greatbritishchefs.com"
