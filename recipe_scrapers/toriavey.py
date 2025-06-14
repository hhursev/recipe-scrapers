from ._abstract import AbstractScraper


class ToriAvey(AbstractScraper):
    @classmethod
    def host(cls):
        return "toriavey.com"
