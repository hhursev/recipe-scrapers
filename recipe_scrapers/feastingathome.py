from ._abstract import AbstractScraper


class FeastingAtHome(AbstractScraper):
    @classmethod
    def host(cls):
        return "feastingathome.com"
