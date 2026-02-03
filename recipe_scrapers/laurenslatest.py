from ._abstract import AbstractScraper


class LaurensLatest(AbstractScraper):
    @classmethod
    def host(cls):
        return "laurenslatest.com"
