from ._abstract import AbstractScraper


class FamilySpice(AbstractScraper):
    @classmethod
    def host(cls):
        return "familyspice.com"
