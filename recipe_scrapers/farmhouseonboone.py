from ._abstract import AbstractScraper


class FarmhouseOnBoone(AbstractScraper):
    @classmethod
    def host(cls):
        return "farmhouseonboone.com"
