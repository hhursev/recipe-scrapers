from ._abstract import AbstractScraper


class TheLoopyWhisk(AbstractScraper):
    @classmethod
    def host(cls):
        return "theloopywhisk.com"
