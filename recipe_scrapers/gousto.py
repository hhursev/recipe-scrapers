from ._abstract import AbstractScraper


# TODO: Remove? Switching over to GoustoJson 2022-08-01
class Gousto(AbstractScraper):
    @classmethod
    def host(cls):
        return "gousto.co.uk"
