from ._abstract import AbstractScraper


class EatThisMuch(AbstractScraper):
    @classmethod
    def host(cls):
        return "eatthismuch.com"

    def site_name(self):
        return "Eat This Much"
