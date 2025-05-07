from ._abstract import AbstractScraper


class NotEnoughCinnamon(AbstractScraper):
    @classmethod
    def host(cls):
        return "notenoughcinnamon.com"
