from ._abstract import AbstractScraper


class TheFoodieTakesFlight(AbstractScraper):
    @classmethod
    def host(cls):
        return "thefoodietakesflight.com"
