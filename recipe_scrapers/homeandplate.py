from ._abstract import AbstractScraper


class HomeAndPlate(AbstractScraper):
    @classmethod
    def host(cls):
        return "homeandplate.com"
