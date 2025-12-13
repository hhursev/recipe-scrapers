from ._abstract import AbstractScraper


class Jow(AbstractScraper):
    @classmethod
    def host(cls):
        return "jow.fr"
