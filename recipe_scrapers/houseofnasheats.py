from ._abstract import AbstractScraper


class HouseOfNashEats(AbstractScraper):
    @classmethod
    def host(cls):
        return "houseofnasheats.com"
