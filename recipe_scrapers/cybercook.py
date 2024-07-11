from ._abstract import AbstractScraper


class Cybercook(AbstractScraper):
    @classmethod
    def host(cls):
        return "cybercook.com.br"
