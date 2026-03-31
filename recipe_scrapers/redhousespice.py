from ._abstract import AbstractScraper


class RedHouseSpice(AbstractScraper):
    @classmethod
    def host(cls):
        return "redhousespice.com"
