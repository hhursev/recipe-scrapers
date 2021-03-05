from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class Przepisy(AbstractScraper):
    @classmethod
    def host(cls):
        return "przepisy.pl"

    def title(self):
        return self.soup.find("h1", {"class": "title"}).get_text()

    def total_time(self):
        return get_minutes(self.soup.find("div", {"class": "time-count"}))

    def yields(self):
        return get_yields(self.soup.find("div", {"class": "person-count"}))

    def ingredients(self):
        ingredients = self.soup.findAll("span", {"class": "text-bg-white"})

        return [
            normalize_string(i.get_text()) + " " + normalize_string(j.get_text())
            for i, j in zip(ingredients[0::2], ingredients[1::2])
        ]

    def instructions(self):
        instructions = self.soup.findAll("p", {"class": "step-info-description"})

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
