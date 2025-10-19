from ._abstract import AbstractScraper


class TheSuburbanSoapBox(AbstractScraper):
    @classmethod
    def host(cls):
        return "thesuburbansoapbox.com"
