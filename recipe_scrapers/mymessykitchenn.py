from ._abstract import AbstractScraper


class MyMessyKitchenn(AbstractScraper):
    @classmethod
    def host(cls):
        return "mymessykitchenn.com"
