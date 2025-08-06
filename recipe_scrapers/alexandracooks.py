from ._abstract import AbstractScraper


class AlexandraCooks(AbstractScraper):
    @classmethod
    def host(cls):
        return "alexandracooks.com"
