from ._abstract import AbstractScraper


class LittleSpiceJar(AbstractScraper):
    @classmethod
    def host(cls):
        return "littlespicejar.com"
