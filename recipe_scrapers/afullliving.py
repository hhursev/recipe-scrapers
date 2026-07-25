from ._abstract import AbstractScraper


class AFullLiving(AbstractScraper):
    @classmethod
    def host(cls):
        return "afullliving.com"
