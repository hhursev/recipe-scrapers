from ._abstract import AbstractScraper


class SavoryThoughts(AbstractScraper):
    @classmethod
    def host(cls):
        return "savorythoughts.com"
