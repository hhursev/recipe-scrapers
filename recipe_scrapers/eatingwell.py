from ._abstract import AbstractScraper


class EatingWell(AbstractScraper):
    @classmethod
    def host(self):
         return "eatingwell.com"