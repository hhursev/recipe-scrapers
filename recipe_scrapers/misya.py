from ._abstract import AbstractScraper


class Misya(AbstractScraper):

    @classmethod
    def host(self):
        return 'misya.info'
