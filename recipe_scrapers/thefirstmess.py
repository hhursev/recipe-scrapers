from ._abstract import AbstractScraper


class TheFirstMess(AbstractScraper):
    @classmethod
    def host(cls):
        return "thefirstmess.com"
