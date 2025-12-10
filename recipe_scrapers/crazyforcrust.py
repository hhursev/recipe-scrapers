from ._abstract import AbstractScraper


class CrazyForCrust(AbstractScraper):
    @classmethod
    def host(cls):
        return "crazyforcrust.com"
