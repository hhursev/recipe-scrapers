from ._abstract import AbstractScraper


class HouseOfYumm(AbstractScraper):
    @classmethod
    def host(cls):
        return "houseofyumm.com"
