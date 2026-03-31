from ._abstract import AbstractScraper


class FigJar(AbstractScraper):
    @classmethod
    def host(cls):
        return "figjar.com"
