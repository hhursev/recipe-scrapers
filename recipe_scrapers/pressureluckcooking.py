from ._abstract import AbstractScraper


class PressureLuckCooking(AbstractScraper):
    @classmethod
    def host(cls):
        return "pressureluckcooking.com"
