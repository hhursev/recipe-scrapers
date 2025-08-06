from ._abstract import AbstractScraper


class MadensVerden(AbstractScraper):
    @classmethod
    def host(cls):
        return "madensverden.dk"
