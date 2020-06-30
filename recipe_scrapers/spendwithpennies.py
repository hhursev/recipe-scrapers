from ._abstract import AbstractScraper


class SpendWithPennies(AbstractScraper):

    @classmethod
    def host(self):
        return 'spendwithpennies.com'
