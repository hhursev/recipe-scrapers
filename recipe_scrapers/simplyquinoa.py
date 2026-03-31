from ._abstract import AbstractScraper


class SimplyQuinoa(AbstractScraper):
    @classmethod
    def host(cls):
        return "simplyquinoa.com"
