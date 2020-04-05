from ._abstract import AbstractScraper


class Cybercook(AbstractScraper):

    @classmethod
    def host(self):
        return 'cybercook.com.br'
