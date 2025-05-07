from ._abstract import AbstractScraper


class SimpleGreenSmoothies(AbstractScraper):
    @classmethod
    def host(cls):
        return "simplegreensmoothies.com"
