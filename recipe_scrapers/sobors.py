from ._abstract import AbstractScraper


class SoBors(AbstractScraper):
    @classmethod
    def host(cls):
        return "sobors.hu"
