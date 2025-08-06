from ._abstract import AbstractScraper


class SwissMilk(AbstractScraper):
    @classmethod
    def host(cls):
        return "swissmilk.ch"
