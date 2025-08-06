from ._abstract import AbstractScraper


class Hostthetoast(AbstractScraper):
    @classmethod
    def host(cls):
        return "hostthetoast.com"
