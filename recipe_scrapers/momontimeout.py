from ._abstract import AbstractScraper


class MomOnTimeout(AbstractScraper):
    @classmethod
    def host(cls):
        return "momontimeout.com"
