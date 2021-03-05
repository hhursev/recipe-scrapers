from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class SimplyRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "simplyrecipes.com"

    def title(self):
        return self.soup.find("h1").get_text()

    def total_time(self):
        return get_minutes(
            self.soup.find("div", {"class": "total-time"})
            .find("span", {"class": "meta-text__data"})
            .text
        )

    def yields(self):
        return get_yields(
            normalize_string(
                self.soup.find("div", {"class": "recipe-serving"})
                .find("span", {"class": "meta-text__data"})
                .text
            )
        )

    def ingredients(self):
        ingredients = self.soup.find("ul", {"class": "ingredient-list"}).findAll("li")

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        steps = self.soup.find(
            "div", {"class": "structured-project__steps"}
        ).ol.findAll("li")

        return "\n".join(
            [
                normalize_string(
                    step.div.text + ": " + "".join([p.text for p in step.findAll("p")])
                )
                for step in steps
            ]
        )
