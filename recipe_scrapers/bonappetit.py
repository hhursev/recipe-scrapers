from ._abstract import AbstractScraper


class BonAppetit(AbstractScraper):
    @classmethod
    def host(cls):
        return "bonappetit.com"

    def total_time(self):
        return None
