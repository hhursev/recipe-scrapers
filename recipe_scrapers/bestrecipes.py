from ._abstract import AbstractScraper
from ._exceptions import StaticValueException


class BestRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "bestrecipes.com.au"

    def language(self):
        raise StaticValueException(return_value="en-AU")
