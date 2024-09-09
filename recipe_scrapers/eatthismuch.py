from ._abstract import AbstractScraper
from ._exceptions import StaticValueException


class EatThisMuch(AbstractScraper):
    @classmethod
    def host(cls):
        return "eatthismuch.com"

    def site_name(self):
        raise StaticValueException(return_value="Eat This Much")

    def author(self):
        raise StaticValueException(return_value="Eat This Much")
