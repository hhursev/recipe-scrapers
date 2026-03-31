from ._abstract import AbstractScraper


class KennethTemple(AbstractScraper):
    @classmethod
    def host(cls):
        return "kennethtemple.com"
