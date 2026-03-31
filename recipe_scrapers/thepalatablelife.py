from ._abstract import AbstractScraper


class ThePalatableLife(AbstractScraper):
    @classmethod
    def host(cls):
        return "thepalatablelife.com"
