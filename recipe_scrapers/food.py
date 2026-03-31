from ._abstract import AbstractScraper
from ._exceptions import StaticValueException


class Food(AbstractScraper):
    @classmethod
    def host(cls):
        return "food.com"

    def site_name(self):
        raise StaticValueException(return_value="Food.com")
