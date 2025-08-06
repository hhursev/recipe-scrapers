from ._abstract import AbstractScraper


class SweetCsDesigns(AbstractScraper):
    @classmethod
    def host(cls):
        return "sweetcsdesigns.com"
