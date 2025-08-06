from ._abstract import AbstractScraper
from ._exceptions import StaticValueException
from ._utils import get_yields, normalize_string


class Przepisy(AbstractScraper):
    @classmethod
    def host(cls):
        return "przepisy.pl"

    def site_name(self):
        raise StaticValueException(return_value="Przepisy.pl")

    def yields(self):
        return get_yields(self.soup.find("div", {"class": "person-count"}))

    def ingredients(self):
        ingredients = self.soup.findAll("span", {"class": "text-bg-white"})

        return [
            normalize_string(i.get_text()) + " " + normalize_string(j.get_text())
            for i, j in zip(ingredients[0::2], ingredients[1::2])
        ]
