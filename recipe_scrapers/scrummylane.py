from ._abstract import AbstractScraper


class ScrummyLane(AbstractScraper):
    @classmethod
    def host(cls):
        return "scrummylane.com"
