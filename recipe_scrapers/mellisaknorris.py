from ._abstract import AbstractScraper


class MellisaKNorris(AbstractScraper):
    @classmethod
    def host(cls):
        return "melissaknorris.com"
