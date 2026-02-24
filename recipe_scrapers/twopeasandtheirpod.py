from ._abstract import AbstractScraper


class TwoPeasAndTheirPod(AbstractScraper):
    @classmethod
    def host(cls):
        return "twopeasandtheirpod.com"
