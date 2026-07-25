from ._abstract import AbstractScraper


class GirlGoneGourmet(AbstractScraper):
    @classmethod
    def host(cls):
        return "girlgonegourmet.com"
