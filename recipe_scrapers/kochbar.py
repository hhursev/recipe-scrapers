from ._abstract import AbstractScraper


class Kochbar(AbstractScraper):

    @classmethod
    def host(self):
        return 'kochbar.de'
