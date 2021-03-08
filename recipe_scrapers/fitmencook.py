from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class FitMenCook(AbstractScraper):
    @classmethod
    def host(cls):
        return "fitmencook.com"

    def title(self):
        raw_title = self.soup.find("h2", {"class": "gap-none"}).get_text()
        title = raw_title.replace("\t", "")
        title = title.replace("\n", "")

        return title

    def total_time(self):
        return get_minutes(self.soup.find("span", {"class": "total-time"}))

    def yields(self):
        for h4 in self.soup.findAll("h4"):
            for strong in h4.findAll("strong"):
                raw_yield = strong.text
                for word in raw_yield.split():
                    if word.isdigit():
                        yields = word

        return get_yields("{} servings".format(yields))

    def ingredients(self):
        ingredients_parent = self.soup.find("div", {"class": "recipe-ingredients"})
        ingredients = ingredients_parent.findAll("li")

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions_parent = self.soup.find("div", {"class": "recipe-steps"})
        instructions = instructions_parent.findAll("li")

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
