from ._abstract import AbstractScraper


class JustineSnacks(AbstractScraper):
    @classmethod
    def host(cls):
        return "justinesnacks.com"
