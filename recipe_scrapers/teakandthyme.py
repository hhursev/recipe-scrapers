from ._abstract import AbstractScraper


class TeakAndThyme(AbstractScraper):
    @classmethod
    def host(cls):
        return "teakandthyme.com"
