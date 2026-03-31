from ._abstract import AbstractScraper


class CreativeCanning(AbstractScraper):
    @classmethod
    def host(cls):
        return "creativecanning.com"
