from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields


class AmazingOriental(AbstractScraper):
    @classmethod
    def host(cls):
        return "amazingoriental.com"

    def title(self):
        return self.soup.find("h1").get_text()

    def category(self):
        return self.soup.select("div.recipe-info .meal-type")[0].get_text()

    def total_time(self):
        return get_minutes(self.soup.select("dl.prepare-time dd")[0].get_text())

    def yields(self):
        return get_yields(self.soup.select(".person-amount")[0].get_text())

    def ingredients(self):
        ingredients = self.soup.select(".sidebar .ingredients-wrap ul li")
        return [" ".join(ingredient.get_text().split()) for ingredient in ingredients]

    def instructions(self):
        instructions = self.soup.select(".main-wrap ul li")
        return "\n".join(instruction.get_text() for instruction in instructions)

    def cuisine(self):
        return self.soup.select("div.sidebar span.category")[0].get_text()
