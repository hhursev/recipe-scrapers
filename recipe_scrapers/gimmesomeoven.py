from ._abstract import AbstractScraper


class GimmeSomeOven(AbstractScraper):
    @classmethod
    def host(cls):
        return "gimmesomeoven.com"
