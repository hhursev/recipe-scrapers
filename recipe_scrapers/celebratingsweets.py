from ._abstract import AbstractScraper


class CelebratingSweets(AbstractScraper):
    @classmethod
    def host(cls):
        return "celebratingsweets.com"
