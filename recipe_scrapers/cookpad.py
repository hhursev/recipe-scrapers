from ._abstract import AbstractScraper


class CookPad(AbstractScraper):

    @classmethod
    def host(self):
        return 'cookpad.com'
