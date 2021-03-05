from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class JamieOliver(AbstractScraper):
    @classmethod
    def host(cls):
        return "jamieoliver.com"

    def title(self):
        return self.soup.find("h1").get_text()

    def total_time(self):
        return get_minutes(self.soup.find("div", {"class": "time"}))

    def yields(self):
        return get_yields(self.soup.find("div", {"class": "recipe-detail serves"}))

    def image(self):
        container = self.soup.find("div", {"class": "recipe-header-left"})
        if not container:
            return None

        image = container.find("img", {"src": True})
        return image["src"] if image else None

    def ingredients(self):
        ingredients = self.soup.find("ul", {"class", "ingred-list"}).findAll("li")
        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = self.soup.find("ol", {"class": "recipeSteps"}).findAll("li")
        return "\n".join([normalize_string(inst.get_text()) for inst in instructions])
