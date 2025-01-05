from ._abstract import AbstractScraper


class LaCucinaItaliana(AbstractScraper):
    @classmethod
    def host(cls):
        return "lacucinaitaliana.it"
