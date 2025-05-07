from ._abstract import AbstractScraper


class ThisHealthyTable(AbstractScraper):
    @classmethod
    def host(cls):
        return "thishealthytable.com"
