from ._abstract import AbstractScraper


class SandwhichTribunal(AbstractScraper):
    @classmethod
    def host(cls):
        return "sandwichtribunal.com"
