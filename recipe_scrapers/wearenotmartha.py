from ._abstract import AbstractScraper


class WeAreNotMartha(AbstractScraper):
    @classmethod
    def host(cls):
        return "wearenotmartha.com"
