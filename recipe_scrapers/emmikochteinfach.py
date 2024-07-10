from ._abstract import AbstractScraper


class EmmiKochtEinfach(AbstractScraper):
    @classmethod
    def host(cls):
        return "emmikochteinfach.de"
