from ._abstract import AbstractScraper


class EverydayPie(AbstractScraper):
    @classmethod
    def host(cls):
        return "everydaypie.com"
