from ._abstract import AbstractScraper


class ImWorthy(AbstractScraper):
    @classmethod
    def host(cls):
        return "im-worthy.com"
