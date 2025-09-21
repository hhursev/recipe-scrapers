from ._abstract import AbstractScraper


class WyseGuide(AbstractScraper):
    @classmethod
    def host(cls):
        return "wyseguide.com"
