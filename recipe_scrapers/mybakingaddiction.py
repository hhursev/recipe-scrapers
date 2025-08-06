from ._abstract import AbstractScraper


class MyBakingAddiction(AbstractScraper):
    @classmethod
    def host(cls):
        return "mybakingaddiction.com"
