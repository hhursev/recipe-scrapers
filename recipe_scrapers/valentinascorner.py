from ._abstract import AbstractScraper


class ValentinasCorner(AbstractScraper):
    @classmethod
    def host(cls):
        return "valentinascorner.com"
