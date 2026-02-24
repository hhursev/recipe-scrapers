from ._abstract import AbstractScraper


class GirlVersusDough(AbstractScraper):
    @classmethod
    def host(cls):
        return "girlversusdough.com"
