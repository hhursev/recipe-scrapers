from ._abstract import AbstractScraper


class CaioFlorentina(AbstractScraper):
    @classmethod
    def host(cls):
        return "ciaoflorentina.com"
