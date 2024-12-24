from ._abstract import AbstractScraper


class PurelyPope(AbstractScraper):
    @classmethod
    def host(cls):
        return "purelypope.com"
