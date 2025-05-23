from ._abstract import AbstractScraper


class TheSpiceTrain(AbstractScraper):
    @classmethod
    def host(cls):
        return "thespicetrain.com"
