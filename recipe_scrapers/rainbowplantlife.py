from ._abstract import AbstractScraper


class RainbowPlantLife(AbstractScraper):
    @classmethod
    def host(cls):
        return "rainbowplantlife.com"
