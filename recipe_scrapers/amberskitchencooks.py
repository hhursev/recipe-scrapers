from ._abstract import AbstractScraper


class AmbersKitchencooks(AbstractScraper):
    @classmethod
    def host(cls):
        return "amberskitchencooks.com"
