from ._abstract import AbstractScraper


class LaCucinaItaliana(AbstractScraper):
    @classmethod
    def host(cls):
        return "lacucinaitaliana.it"
    
    def author(self):
        return "La Cucina Italiana"
