from ._abstract import AbstractScraper


class Misya(AbstractScraper):
    @classmethod
    def host(cls):
        return "misya.info"
