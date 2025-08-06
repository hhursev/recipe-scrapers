from ._abstract import AbstractScraper


class AverieCooks(AbstractScraper):
    @classmethod
    def host(cls):
        return "averiecooks.com"
