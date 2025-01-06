from ._abstract import AbstractScraper


class LaCucinaItaliana(AbstractScraper):
    @classmethod
    def host(cls, domain="it"):
        return f"lacucinaitaliana.{domain}"

    def author(self):
        return "La Cucina Italiana"
