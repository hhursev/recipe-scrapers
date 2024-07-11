from ._abstract import AbstractScraper


class TheKitchn(AbstractScraper):
    @classmethod
    def host(cls):
        return "thekitchn.com"
